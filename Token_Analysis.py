import os, sys, csv, datetime
from PSDecode import PSDecode # Powershell Decorations
from PSDetect import PSDetect # Obfuscation Detection
from SynDict import Dict_Check # Syntax Dictionary Module
from SynDict import Dict_Update
from PSTokenize import PSTokenize # Token extraction using PSParser

# ===== Be sure to run in PowerShell! =====
# Hybrid Syntax Dictionary (fully active + partially active)
# Final Amendment: 2020/09/23 (Version 1.9.15)
# Translation : 2021/04/29
# ==============================
# 1. Seq_Process(Type, Num) - Sequence Numbering (Type, Sequence Start, Token Value) / Return Value (INT): Sequence Number
# 2. main() - Main Function
# ==============================

def Seq_Process(Type, Num, Token): # Sequence Numbering (Type, Sequence Start, Token Value)
    #global Command_Dict, Argument_Dict, Parameter_Dict, Keyword_Dict, Variable_Dict
    if(Type == "Command"):
        for word in Command_Dict:
            word = word.rstrip() # Remove Return Code (Remove String Blank)
            if (word == Token.lower()):
                return Num
            Num = Num + 1
            
    if(Type == "CommandArgument"):
        for word in Argument_Dict:
            word = word.rstrip() # Remove Return Code (Remove String Blank)
            if (word == Token.lower()):
                return Num
            Num = Num + 1
            
    if(Type == "CommandParameter"):
        for word in Parameter_Dict:
            word = word.rstrip() # Remove Return Code (Remove String Blank)
            if (word == Token.lower()):
                return Num
            Num = Num + 1
            
    if(Type == "Keyword"):
        for word in Keyword_Dict:
            word = word.rstrip() # Remove Return Code (Remove String Blank)
            if (word == Token.lower()):
                return Num
            Num = Num + 1
            
    if(Type == "Variable"):
        for word in Variable_Dict:
            word = word.rstrip() # Remove Return Code (Remove String Blank)
            if (word == Token.lower()):
                return Num
            Num = Num + 1

    Num = Num + 1

    # Add Syntax Dictionary if not in Syntax Dictionary
    if(Type == "Command"):
        Command_Dict.append(Token.lower())
    if(Type == "CommandArgument"):
        Argument_Dict.append(Token.lower())
    if(Type == "CommandParameter"):
        Parameter_Dict.append(Token.lower())
    if(Type == "Keyword"):
        Keyword_Dict.append(Token.lower())
    if(Type == "Variable"):
        Variable_Dict.append(Token.lower())
        
    return Num



def main():
    # Prepare files for analysis
    FileDir = "D:\\Analysis_Files" # Directory to navigate to
    FilePath = FileDir + "\\"
    FileName = os.listdir(FileDir)
    FileLimit = 0  # Size Limit (KB) - Unlimited to 0

    # Output File (Filename - Number)
    Output_Name = "Output_CSV"
    Output_Setup = True  # If true, erase already existing files and recreate / False is an earwrite

    # Prepare Pre-File (Renew)
    global Command_Dict, Argument_Dict, Parameter_Dict, Keyword_Dict, Variable_Dict
    Command_Dict = Dict_Check("Command_Dict.txt")
    Argument_Dict = Dict_Check("CommandArgument_Dict.txt")
    Parameter_Dict = Dict_Check("CommandParameter_Dict.txt")
    Keyword_Dict = Dict_Check("Keyword_Dict.txt")
    Variable_Dict = Dict_Check("Variable_Dict.txt")

    # Program Main
    print ("-----------------------------------------------------")
    print("PowerShell Token Analysis  (v1.9.16)")
    print ("-----------------------------------------------------")
    F_Time = datetime.datetime.now()  # Start Time Logging for Analysis Time Recording
    Search = ['Command', 'CommandArgument', 'CommandParameter', 'Keyword', 'Variable'] # 검색할 토큰
    FileMax = len(FileName)
    print("* Total Files : " , FileMax)
    FileCount = 0 # Count to show progress
    Output_Dict = [] # Temporary Dictionary
    Decode_Remove = False # Dedicate data temporary file removal status
    
    CSV_Cut = input("* Enter split units (quantities) : ") # Do not split when entering 0
    CSV_Filecount = 1
    CSV_Count = 1
    

    for Name in FileName:
        FileCount = FileCount + 1
        PATH = FilePath + Name
        Output_Data = Name # Temporary variable containing output data

        # Analytical Size Limit
        FileSize = os.path.getsize(PATH)
        if(FileLimit > 0 and FileSize > FileLimit * 1024):
            print("** We do not analyze this file due to capacity limitations. ")
            continue
            

        # Check for obfuscation
        if(PSDetect(PATH)):
            print ("[Obfuscation] - " + Name + "  (" + str(FileCount) + "/" + str(FileMax) +")")
            PATH = PSDecode(PATH) # Decryption Attempts
            Output_Dict = PSTokenize(PATH, Search) # Extract Tokens with PSParser
            if (Decode_Remove): # Decryption Temporary Data Deletion
                os.remove(PATH, 3)
                
        else:
            print("[Normal] - " + Name + " (" + str(FileCount) + "/" + str(FileMax) + ")")
            Output_Dict = PSTokenize(PATH, Search) # Extract Tokens with PSParser
        
        # Sequence Processing
        for N in range(0, len(Output_Dict)):
            Seq_tmp = Output_Dict[N].split("===")

            # Sequence Number Output
            if(Seq_tmp[0] == "Command"):
                Output_Data = Output_Data + "," + str(Seq_Process("Command", 1, Seq_tmp[1]))
            elif(Seq_tmp[0] == "CommandArgument"):
                Output_Data = Output_Data + "," + str(Seq_Process("CommandArgument", 2000, Seq_tmp[1]))
            elif(Seq_tmp[0] == "CommandParameter"):
                Output_Data = Output_Data + "," + str(Seq_Process("CommandParameter", 4000, Seq_tmp[1]))
            elif(Seq_tmp[0] == "Keyword"):
                Output_Data = Output_Data + "," + str(Seq_Process("Keyword", 8000, Seq_tmp[1]))
            elif(Seq_tmp[0] == "Variable"):
                Output_Data = Output_Data + "," + str(Seq_Process("Variable", 10000, Seq_tmp[1]))

        if Output_Setup and not CSV_Count:  # When initializing a file
            Output_F = open(Output_Name + "-" + str(CSV_Filecount) + ".csv", 'w')
            
        Output_F = open(Output_Name + "-" + str(CSV_Filecount) + ".csv", 'a')
        # Except if there is no sequence!
        Output_len = Output_Data.split(',')
        if (len(Output_len) > 2):
            Output_F.write(Output_Data + '\n') # Input
            CSV_Count = CSV_Count + 1
            
            if not int(CSV_Cut) == 0 and int(CSV_Cut) < CSV_Count:  # If CSV_Count exceeds a specified number of sequences
                CSV_Filecount = CSV_Filecount + 1
                CSV_Count = 1

    Output_F.close()
    print ("-----------------------------------------------------")
    print ("Updating syntax dictionary...")

    Dict_Update("Command_Dict.txt", Command_Dict)
    Dict_Update("CommandArgument_Dict.txt", Argument_Dict)
    Dict_Update("CommandParameter_Dict.txt", Parameter_Dict)
    Dict_Update("Keyword_Dict.txt", Keyword_Dict)
    Dict_Update("Variable_Dict.txt", Variable_Dict)

    print ("-----------------------------------------------------")
    L_Time = datetime.datetime.now()
    print("Analysis Time : ", L_Time - F_Time)  # Analysis Time (Minutes)
    if CSV_Filecount > 1:
        CSV_FileCount - 1
    print("Number of files generated : ", CSV_Filecount)
    print ("Finish!")    
    

if __name__ == '__main__':
    main()


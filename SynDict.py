import os, sys

# SynDict : SynDict : Syntax Dictionary Module
# -----------------------------------------------------------------------------------------------
# 1. Dict_Check (File) - Syntax Precheck (file name)
# 2. Dict_Update (File, Dict) - Syntax dictionary update (file name, dictionary array)
# 3. Dict_Keyword (File) - Keyword token dictionary update (file name)
# Translation : 2021/04/29
# -----------------------------------------------------------------------------------------------

def Dict_Check(File): # Syntax pre-check (file name)
    print("File Check : " + File)
    Dict_out = []

    try:
        Dict_F = open("Dict\\" + File, 'r')
        Dict = Dict_F.readlines()
        for word in Dict:
            word = word.rstrip() # Remove \n at the end of the sentence
            Dict_out.append(word)
            Dict_F.close()
            
    except FileNotFoundError:
        if File == "Keyword_Dict.txt":
            Dict_Keyword(File)
        else:
            print("- " + File + " File not found, creating a new one.")
            Dict_F = open("Dict\\" + File, 'w')
            Dict_F.close()
        
    return Dict_out


def Dict_Update(File, Dict):  # Syntax dictionary update (file name, dictionary array)
    Dict_F = open("Dict\\" + File, 'w')

    for word in Dict:
        Dict_F.write(word + '\n')

    Dict_F.close()
    return


def Dict_Keyword(File):  # Keyword token dictionary update
    Keyword_Data = [
        "keyword", 
        "for", 
        "if", 
        "param", 
        "process", 
        "function", 
        "foreach", 
        "in", 
        "else", 
        "try", 
        "catch", 
        "return", 
        "throw", 
        "elseif", 
        "switch", 
        "while", 
        "configuration", 
        "node", 
        "registry", 
        "testregistry", 
        "exit", 
        "break"
    ]

    Dict_F = open("Dict\\" + File, 'w')

    for word in Keyword_Data:
        Dict_F.write(word + '\n')

    Dict_F.close()
    return


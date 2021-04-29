import subprocess, locale

# -----------------------------------------------------------------------------------------------
# 1. PSDecode (File): Decryption module using PSDecode
# Return value (String): 0 - When decryption fails / [String] - When decryption
# Translation : 2021/04/29
# -----------------------------------------------------------------------------------------------

def PSDecode(File):
    command = "powershell.exe Get-Content " + File + " | PSDecode;"
    # Invoke command to Subprocess
    ps = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    data, err = ps.communicate()

    # Decode the results to fit the system
    lang = locale.getdefaultlocale() # Import Operating System Language
    # Use second value because the resulting value of lang is (language, encoding)
    try:
        data = data.decode(lang[1])
        err = err.decode(lang[1])
    except UnicodeDecodeError:  # In case of Unicode error
        try:
            data = data.decode('UTF-8')
            err = err.decode('UTF-8')
        except:
            return 0  # Returns 0 if an error still occurs
        

    if(err != ""):
        print("==========[Error]==========")
        print("Either it was not run in PowerShell or the PSDecode module was not installed.")
        return 0

    Check = False # Save Detections Successful
    Output = [] # Variables to hold results on successful decryption
    Del_output = 0 # Variables to remember unnecessary lines of data

    dataline = data.split('\n')

    for word in dataline:
        Checkline = word[31:38]

        if(Check):
            if(word == ""):
                Check = False
            if not word[0:10] == "No actions":  # No actions Identified. Methods~~  Remove Phrase
                Output.append(word) # Adding decryption data to the output file
                Del_output = Del_output + 1

        for N in range(3, 1, -1):
            if(Checkline == "Layer " + str(N)): # On successful decryption
                Check = True
                continue

        if "### Actions ###" in word:
            Check = True
            continue
        elif "### Warning! ###" in word: # On alert
            if (Check): # If decryption is successful and "Warning" appears,
                del Output[len(Output)-1] # ### Warning! ### remove
                break

            return 0 # Otherwise, return as Decryption Failed
        elif "### ERROR! ###" in word: # When Decryption Fails
            return 0 # return Fails


    Decode_File = open(File + "_decode", 'w', encoding='UTF-8') # Creating a Decoded Temporary File

    Num = 1
    for dataline in Output: # Write File
        if(Num == Del_output):
            break
        
        Decode_File.write(dataline)
        Num = Num + 1
    
    Decode_File.close()
    return File + "_decode"

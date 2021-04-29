import subprocess, locale

# PSTokenize: PowerShell Token Extraction Module with PSParser
# -----------------------------------------------------------------------------------------------
# 1. PSTokenize (File) - PowerShell Token Extraction (File, Search Token[]) - Return Value (String[]): Temporary Dictionary
# Translation : 2021/04/29
# -----------------------------------------------------------------------------------------------

def PSTokenize(File, Search):
    ps = subprocess.Popen('powershell.exe $Tokens = [System.Management.Automation.PSParser]::Tokenize((Get-Content \'%s\'), [ref]$null); \
            echo $Tokens'%File, stdout = subprocess.PIPE).stdout

    # Decode the results to fit the system
    lang = locale.getdefaultlocale() # Get OS Language
    try:
        Data = ps.read().strip().decode(lang[1])
    except UnicodeDecodeError:  # If Unicode Error
        try:
            Data = ps.read().strip().decode('UTF-8')
        except:
            return 0  # Returns 0 if an error still occurs

    Word = Data.split('\n') # Divide data by lines

    Tmp = "" # Temporary variable remembering previous line
    Output_Dict = [] # A temporary dictionary that stores the result values

    for N in range(0, len(Word)):
        try:
            Word[N] = Word[N].rstrip() # Remove String Return Code (Remove Blank Characters)
        except:
            pass

        for S_Token in Search:
            # Debug Code
            #print("----------------------")
            #print("[", N, "]  LAST : ", Tmp) #COMMAND
            #print("[", N, "]  Type : ", S_Token)
            #print("[", N, "]  Word : ", Word[N])
            #print(Word[N][14:])
            if (Word[N][14:] == S_Token):
                Process_Word = Tmp[14:] # Remove "Content : " before
                Output_Dict.append(S_Token + "===" + Process_Word)

        Tmp = Word[N]

    return Output_Dict

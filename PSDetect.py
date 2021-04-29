import os, sys, subprocess, locale

# -----------------------------------------------------------------------------------------------
# 1. PSDetect: Inspect powershell code for obfuscation using Revoke-Obfuscation
# Return value (INT): 0 - Denomination / 1 - Obfuscation
# Translation : 2021/04/29
# -----------------------------------------------------------------------------------------------

def PSDetect(file):
    command = "powershell.exe Get-Content " + file + " | Measure-RvoObfuscation -verbose;"
    # Invoke command to Subprocess
    ps = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    data, err = ps.communicate()

    # Decode the results to fit the system
    lang = locale.getdefaultlocale() # Get OS Language
    # Use second value because the resulting value of lang is (language, encoding)
    try:
        data = data.decode(lang[1])
        err = err.decode(lang[1])
    except UnicodeDecodeError:  # If Unicode Error
        try:
            data = data.decode('UTF-8')
            err = err.decode('UTF-8')
        except:
            return 0

    dataline = data.split('\n')

    if(err != ""):
        #print("==========[Error]==========")
        #print("The Revoke-Obfuscation module is not installed or not running in PowerShell. ")
        return 0

    if(dataline[0][9:19] == "OBFUSCATED"): # In case of obfuscation
        return 1
    else:
        return 0

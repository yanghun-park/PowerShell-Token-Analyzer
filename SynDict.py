import os, sys

# SynDict : 구문사전 모듈
# -----------------------------------------------------------------------------------------------
# 1. Dict_Check(File) - 구문사전 확인(파일명)
# 2. Dict_Update(File, Dict) - 구문사전 업데이트(파일명, 사전배열)
# 3. Dict_Keyword(File) - Keyword 토큰사전 업데이트(파일명)
# -----------------------------------------------------------------------------------------------

def Dict_Check(File): # 구문사전 확인(파일명)
    print("파일 확인 : " + File)
    Dict_out = []

    try:
        Dict_F = open("Dict\\" + File, 'r')
        Dict = Dict_F.readlines()
        for word in Dict:
            word = word.rstrip() #문장끝의 \n 제거
            Dict_out.append(word)
            Dict_F.close()
            
    except FileNotFoundError:
        if File == "Keyword_Dict.txt":
            Dict_Keyword(File)
        else:
            print("- " + File + " 파일을 찾을 수 없어 새로 생성합니다.  ")
            Dict_F = open("Dict\\" + File, 'w')
            Dict_F.close()
        
    return Dict_out


def Dict_Update(File, Dict):  # 구문사전 업데이트(파일명, 사전배열)
    Dict_F = open("Dict\\" + File, 'w')

    for word in Dict:
        Dict_F.write(word + '\n')

    Dict_F.close()
    return


def Dict_Keyword(File):  # Keyword 토큰사전 업데이트(파일명)
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


import subprocess, locale

# PSTokenize : PSParser를 사용한 PowerShell 토큰추출 모듈
# -----------------------------------------------------------------------------------------------
# 1. PSTokenize(File) - PowerShell 토큰추출(파일, 검색토큰[]) - 반환값(String[]) : 임시사전
# -----------------------------------------------------------------------------------------------

def PSTokenize(File, Search):
    #command = "'powershell.exe $Tokens = [System.Management.Automation.PSParser]::Tokenize((Get-Content \'%s\'), [ref]$null); \echo $Tokens'%path"
    ps = subprocess.Popen('powershell.exe $Tokens = [System.Management.Automation.PSParser]::Tokenize((Get-Content \'%s\'), [ref]$null); \
            echo $Tokens'%File, stdout = subprocess.PIPE).stdout

    # 결과 내용을 시스템에 맞게 디코드
    lang = locale.getdefaultlocale() # 운영체제 언어 불러오기
    try:
        Data = ps.read().strip().decode(lang[1])
    except UnicodeDecodeError:  # 유니코드 오류시
        try:
            Data = ps.read().strip().decode('UTF-8')
        except:
            return 0  # 그래도 오류가 발생할경우 0 반환

    Word = Data.split('\n') # 데이터를 줄 단위로 나눔

    Tmp = "" # 이전 줄을 기억하는 임시변수
    Output_Dict = [] # 결과값을 저장하는 임시사전

    for N in range(0, len(Word)):
        try:
            Word[N] = Word[N].rstrip() # 문자열 리턴코드 제거(공백문자 제거)
        except:
            pass

        for S_Token in Search:
            # 디버그 코드(print문)
            #print("----------------------")
            #print("[", N, "]  LAST : ", Tmp) #COMMAND
            #print("[", N, "]  Type : ", S_Token)
            #print("[", N, "]  Word : ", Word[N])
            #print(Word[N][14:])
            if (Word[N][14:] == S_Token):
                Process_Word = Tmp[14:] # 앞에 Content : 제거
                Output_Dict.append(S_Token + "===" + Process_Word)

        Tmp = Word[N]

    return Output_Dict

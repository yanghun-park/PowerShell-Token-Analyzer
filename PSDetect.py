import os, sys, subprocess, locale

# -----------------------------------------------------------------------------------------------
# 1. PSDetect : Revoke-Obfuscation을 이용한 파워쉘 코드의 난독화 여부 검사
# 반환값(INT) : 0 - 비난독화 / 1 - 난독화
# -----------------------------------------------------------------------------------------------

def PSDetect(file):
    command = "powershell.exe Get-Content " + file + " | Measure-RvoObfuscation -verbose;"
    # Subprocess로 명령어 호출
    ps = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    data, err = ps.communicate()

    # 결과 내용을 시스템에 맞게 디코드
    lang = locale.getdefaultlocale() # 운영체제 언어 불러오기
    # lang의 결과값은 (언어, 인코딩)이므로 두번째값 사용
    try:
        data = data.decode(lang[1])
        err = err.decode(lang[1])
    except UnicodeDecodeError:  # 유니코드 오류시
        try:
            data = data.decode('UTF-8')
            err = err.decode('UTF-8')
        except:
            return 0  # 그래도 오류가 발생할경우 0 반환

    dataline = data.split('\n')

    if(err != ""):
        #print("==========[오류]==========")
        #print("PowerShell에서 실행되지 않았거나 Revoke-Obfuscation 모듈이 설치되지 않았습니다. ")
        return 0

    if(dataline[0][9:19] == "OBFUSCATED"): # 난독화일 경우
        return 1
    else:
        return 0

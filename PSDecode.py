import subprocess, locale

# -----------------------------------------------------------------------------------------------
# 1. PSDecode(File) : PSDecode를 이용한 복호화 모듈
# 반환값(String) : 0 - 복호화 실패시 / [문자열] - 복호화 성공시
# -----------------------------------------------------------------------------------------------

def PSDecode(File):
    command = "powershell.exe Get-Content " + File + " | PSDecode;"
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
        

    if(err != ""):
        print("==========[오류]==========")
        print("PowerShell에서 실행되지 않았거나 PSDecode 모듈이 설치되지 않았습니다. ")
        return 0

    Check = False # 탐지 성공여부를 저장
    Output = [] # 복호화 성공시 결과를 담을 변수
    Del_output = 0 # 불필요한 데이터 줄을 기억할 변수

    dataline = data.split('\n')

    for word in dataline:
        Checkline = word[31:38]

        if(Check):
            if(word == ""):
                Check = False
            if not word[0:10] == "No actions":  # No actions Identified. Methods~~  문구 제거
                Output.append(word) # 출력 파일에 복호화 데이터 추가
                Del_output = Del_output + 1

        for N in range(3, 1, -1):
            if(Checkline == "Layer " + str(N)): # 복호화 성공시
                Check = True
                continue

        if "### Actions ###" in word:
            Check = True
            continue
        elif "### Warning! ###" in word: # 경고 발생시
            if (Check): # 복호화에 성공했으나 Warning가 뜰 경우
                del Output[len(Output)-1] # ### Warning! ### 제거
                break

            return 0 # 그렇지 않은경우 복호화 실패로 반환
        elif "### ERROR! ###" in word: # 복호화 실패시
            return 0 # 복호화 실패


    Decode_File = open(File + "_decode", 'w', encoding='UTF-8') # 복호화된 임시파일 생성

    Num = 1
    for dataline in Output: # 파일 쓰기
        if(Num == Del_output):
            break
        
        Decode_File.write(dataline)
        Num = Num + 1
    
    Decode_File.close()
    return File + "_decode"

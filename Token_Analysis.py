import os, sys, csv, datetime
from PSDecode import PSDecode # 파워쉘 복호화
from PSDetect import PSDetect # 난독화 탐지
from SynDict import Dict_Check # 구문사전 모듈
from SynDict import Dict_Update
from PSTokenize import PSTokenize # PSParser를 사용한 토큰추출

# ===== 반드시 PowerShell에서 실행! =====
# 하이브리드 구문사전 (완전능동 + 부분능동 결합)
# 최종수정 : 2020/09/23 (Version 1.9.15)
# ==============================
# 1. Seq_Process(Type, Num) - 시퀀스 번호 부여(타입, 시퀀스 시작값, 토큰값) / 반환값(INT) : 시퀀스번호
# 2. main() - 메인함수
# ==============================
# TEST

def Seq_Process(Type, Num, Token): # 시퀀스 번호 부여(타입, 시퀀스 시작값, 토큰값)
    #global Command_Dict, Argument_Dict, Parameter_Dict, Keyword_Dict, Variable_Dict
    if(Type == "Command"):
        for word in Command_Dict:
            word = word.rstrip() # 리턴코드 제거(문자열 공백문자 제거)
            if (word == Token.lower()):
                return Num
            Num = Num + 1
            
    if(Type == "CommandArgument"):
        for word in Argument_Dict:
            word = word.rstrip() # 리턴코드 제거(문자열 공백문자 제거)
            if (word == Token.lower()):
                return Num
            Num = Num + 1
            
    if(Type == "CommandParameter"):
        for word in Parameter_Dict:
            word = word.rstrip() # 리턴코드 제거(문자열 공백문자 제거)
            if (word == Token.lower()):
                return Num
            Num = Num + 1
            
    if(Type == "Keyword"):
        for word in Keyword_Dict:
            word = word.rstrip() # 리턴코드 제거(문자열 공백문자 제거)
            if (word == Token.lower()):
                return Num
            Num = Num + 1
            
    if(Type == "Variable"):
        for word in Variable_Dict:
            word = word.rstrip() # 리턴코드 제거(문자열 공백문자 제거)
            if (word == Token.lower()):
                return Num
            Num = Num + 1

    Num = Num + 1

    # 구문사전에 없을 경우 구문사전 추가
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
    #분석할 파일 준비
    FileDir = "E:\\Analysis_Files\\Test" # 탐색할 디렉토리
    FilePath = FileDir + "\\"
    FileName = os.listdir(FileDir)
    FileLimit = 0  # 크기제한(KB) - 0일경우 제한하지 않음

    # 출력할 파일 (파일명-번호)
    Output_Name = "Output_CSV"
    Output_Setup = True  # True일경우 이미 있는파일을 지우고 재생성 / False는 이어쓰기

    # 사전파일 준비(갱신)
    global Command_Dict, Argument_Dict, Parameter_Dict, Keyword_Dict, Variable_Dict
    Command_Dict = Dict_Check("Command_Dict.txt")
    Argument_Dict = Dict_Check("CommandArgument_Dict.txt")
    Parameter_Dict = Dict_Check("CommandParameter_Dict.txt")
    Keyword_Dict = Dict_Check("Keyword_Dict.txt")
    Variable_Dict = Dict_Check("Variable_Dict.txt")

    # 분석 프로그램 메인
    print ("-----------------------------------------------------")
    print("PowerShell 분석 프로그램  (v1.9.15)")
    print ("-----------------------------------------------------")
    F_Time = datetime.datetime.now()  # 분석시간 기록을 위해 시작시간 기록
    Search = ['Command', 'CommandArgument', 'CommandParameter', 'Keyword', 'Variable'] # 검색할 토큰
    FileMax = len(FileName)
    print("* 총 파일 : " , FileMax)
    FileCount = 0 # 진행상황 표시를 위한 카운트
    Output_Dict = [] # 임시 사전
    Decode_Remove = False # 복호데이터 임시파일 제거여부
    
    CSV_Cut = input("* 분할 단위(수량) 입력 : ") # 0입력시 분할하지 않음
    CSV_Filecount = 1
    CSV_Count = 1
    

    for Name in FileName:
        FileCount = FileCount + 1
        PATH = FilePath + Name
        Output_Data = Name # 출력데이터를 담는 임시변수

        # 분석 크기 제한
        FileSize = os.path.getsize(PATH)
        if(FileLimit > 0 and FileSize > FileLimit * 1024):
            print("** 용량 제한에 의하여 이 파일을 분석하지 않습니다. ")
            continue
            

        # 난독화 여부 검사
        if(PSDetect(PATH)):
            print ("[난독화] - " + Name + "  (" + str(FileCount) + "/" + str(FileMax) +")")
            PATH = PSDecode(PATH) # 복호화 시도
            Output_Dict = PSTokenize(PATH, Search) # PSParser로 토큰추출
            if (Decode_Remove): # 복호화 임시데이터 삭제
                os.remove(PATH, 3)
                
        else:
            print("[정상] - " + Name + " (" + str(FileCount) + "/" + str(FileMax) + ")")
            Output_Dict = PSTokenize(PATH, Search) # PSParser로 토큰추출
        
        # 시퀀스 처리
        for N in range(0, len(Output_Dict)):
            Seq_tmp = Output_Dict[N].split("===")

            #시퀀스 번호 출력
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

        if Output_Setup and not CSV_Count:  # 파일을 초기화를 할 경우
            Output_F = open(Output_Name + "-" + str(CSV_Filecount) + ".csv", 'w')
            
        Output_F = open(Output_Name + "-" + str(CSV_Filecount) + ".csv", 'a')
        # 만약 시퀀스가 없는 경우 제외!
        Output_len = Output_Data.split(',')
        if (len(Output_len) > 2):
            Output_F.write(Output_Data + '\n') # 입력
            CSV_Count = CSV_Count + 1
            
            if not int(CSV_Cut) == 0 and int(CSV_Cut) < CSV_Count:  # 만약 CSV_Count가 정해진 시퀀스수를 초과할 경우
                CSV_Filecount = CSV_Filecount + 1
                CSV_Count = 1

    Output_F.close()
    print ("-----------------------------------------------------")
    print ("구문사전 업데이트중...")

    Dict_Update("Command_Dict.txt", Command_Dict)
    Dict_Update("CommandArgument_Dict.txt", Argument_Dict)
    Dict_Update("CommandParameter_Dict.txt", Parameter_Dict)
    Dict_Update("Keyword_Dict.txt", Keyword_Dict)
    Dict_Update("Variable_Dict.txt", Variable_Dict)

    print ("-----------------------------------------------------")
    L_Time = datetime.datetime.now()
    print("분석시간 : ", L_Time - F_Time)  # 분석시간 분
    if CSV_Filecount > 1:
        CSV_FileCount - 1
    print("생성된 파일 갯수 : ", CSV_Filecount)
    print ("작업이 완료되었습니다. ")    
    

if __name__ == '__main__':
    main()


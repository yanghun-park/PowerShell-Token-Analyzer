import csv, os, datetime

# ===== CSV 병합 프로그램 =====
# 디렉토리내 모든 CSV파일을 하나로 병합
# 최종수정 : 2020/09/16 (Version 1.0.0)
# =========================

def main():
    FileName = "merged_normal.csv" # 출력할 파일
    TaskDir = "CSV_Files" # 작업폴더
    TaskPath = TaskDir + "\\"
    TaskList = os.listdir(TaskDir)
    
    print("---------- CSV 병합 도구 ----------")
    print("* 주의 : 기존에 생성된 파일을 초기화 합니다. ")
    print("* 파일명 : " + FileName)
    print("--------------------------------------")
    first_time = datetime.datetime.now()

    CSV_Output = open(FileName, "w")
    CSV_OUT = [] # 병합 CSV 딕셔너리 생성
    FileCount = 0
    FileMax = len(TaskList)

    for Name in TaskList:
        FileCount = FileCount + 1
        PATH = TaskPath + Name
        print("* 병합중... - " + Name + " (" + str(FileCount) + "/" + str(FileMax) + ")")
        
        CSV_F = open(PATH, 'r') # CSV 파일 읽기
        CSV_Temp = CSV_F.readlines()
        for Line in CSV_Temp:
            Line = Line.rstrip() # 문장끝의 \n 제거
            CSV_OUT.append(Line)


    print("* 최종파일 생성중...")
    for Line in CSV_OUT:
        CSV_Output.write(Line + '\n')

    CSV_Output.close()
    last_time = datetime.datetime.now()
    print("----------------------------")
    print("# 작업이 완료되었습니다. ")
    print("# 경과 시간 : " + str(last_time - first_time))
    print("----------------------------")
    return 0


if __name__ == '__main__':
    main()

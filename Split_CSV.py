import csv, os, datetime

# ===== CSV 분할 프로그램 =====
# 디렉토리내 모든 CSV파일을 하나로 병합
# 최종수정 : 2020/10/16 (Version 1.1.0)
# =========================

def main():
    InputName1 = "merged_normal_old.csv" # 입력할 파일1
    InputName2 = "merged_normal_new.csv"  # 입력할 파일2
    
    OutputName1 = "Output_Normal_old"  # 출력할 파일1 (입력1)
    OutputName2 = "Output_Normal_new"  # 출력할 파일2 (입력2)
    
    print("---------- CSV 분할 도구 ----------")
    print("* 입력된 파일1 : " + InputName1)
    print("* 입력된 파일2 : " + InputName2)
    print("--------------------------------------")
    first_time = datetime.datetime.now()

    CSV_F1 = open(InputName1, 'r')
    CSV_F2 = open(InputName2, 'r')

    F1_Data = CSV_F1.readlines()
    F2_Data = CSV_F2.readlines()
    F1_Head = []
    F2_Head = []

    for Num in range(0, len(F1_Data)-1):
        F1_Split = F1_Data[Num].split(",")
        F1_Head.append(F1_Split[0])

    for Num in range(0, len(F2_Data)-1):
        F2_Split = F2_Data[Num].split(",")
        F2_Head.append(F2_Split[0])

    Final_F1 = []
    Final_F2 = []
    
    for F1 in range(0, len(F1_Data)-1):
        for F2 in range(0, len(F2_Data)-1):
            if F1_Head[F1] == F2_Head[F2]:
                Final_F1.append(F1_Data[F1])
                Final_F2.append(F2_Data[F2])
                
    #print("----- 최종결과값 -----")
    #print(Final_F1)
    #print(len(Final_F1))
    #print(Final_F2)
    #print(len(Final_F2))

    FileCount = 0
    Count = input("몇개 단위로 분할할까요? : ")
    CSV_Count = 0  # CSV 줄 라인 기록
    CSV_Max = len(Final_F1)

    while(True):
        print("- 분할중... / 파일명 : " + OutputName1 + "_" + str(FileCount))
        CSV_Output1 = open(OutputName1 + "_" + str(FileCount) + ".csv", 'w')
        print("- 분할중... / 파일명 : " + OutputName2 + "_" + str(FileCount))
        CSV_Output2 = open(OutputName2 + "_" + str(FileCount) + ".csv", 'w')

        for A in range(CSV_Count, CSV_Count+int(Count)):
            if(CSV_Count >= CSV_Max):  # 모든 처리가 끝나면 종료
                break
            CSV_Output1.write(Final_F1[A])
            CSV_Output2.write(Final_F2[A])
            CSV_Count = CSV_Count+ 1

        CSV_Output1.close()
        CSV_Output2.close()
        
        if(CSV_Count >= CSV_Max):  # 모든 처리가 끝나면 종료
            break

        FileCount = FileCount + 1
        
    last_time = datetime.datetime.now()
    print("----------------------------")
    print("# 작업이 완료되었습니다. ")
    print("# 경과 시간 : " + str(last_time - first_time))
    print("----------------------------")
    return 0


if __name__ == '__main__':
    main()

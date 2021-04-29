import csv, os, datetime

# ===== CSV Segmentation Program =====
# Merge all CSV files in the directory into one
# Final Amendment: 2020/10/16 (Version 1.1.0)
# Translation : 2021/04/29
# =========================

def main():
    InputName1 = "merged_normal_old.csv" # Input File1
    InputName2 = "merged_normal_new.csv"  # Input File2
    
    OutputName1 = "Output_Normal_old"  # Output File1 (Input1)
    OutputName2 = "Output_Normal_new"  # Output FIle2 (Input2)
    
    print("---------- CSV Split Tools ----------")
    print("* Input File1 : " + InputName1)
    print("* Input File2 : " + InputName2)
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

    FileCount = 0
    Count = input("How many units should we divide it into? : ")
    CSV_Count = 0  # CSV Line History
    CSV_Max = len(Final_F1)

    while(True):
        print("- Splitting... / File Name : " + OutputName1 + "_" + str(FileCount))
        CSV_Output1 = open(OutputName1 + "_" + str(FileCount) + ".csv", 'w')
        print("- Splitting... / File Name : " + OutputName2 + "_" + str(FileCount))
        CSV_Output2 = open(OutputName2 + "_" + str(FileCount) + ".csv", 'w')

        for A in range(CSV_Count, CSV_Count+int(Count)):
            if(CSV_Count >= CSV_Max):  # Exit when all processing is complete
                break
            CSV_Output1.write(Final_F1[A])
            CSV_Output2.write(Final_F2[A])
            CSV_Count = CSV_Count+ 1

        CSV_Output1.close()
        CSV_Output2.close()
        
        if(CSV_Count >= CSV_Max):  # Exit when all processing is complete
            break

        FileCount = FileCount + 1
        
    last_time = datetime.datetime.now()
    print("----------------------------")
    print("# Finish!")
    print("# Elapsed Time : " + str(last_time - first_time))
    print("----------------------------")
    return 0


if __name__ == '__main__':
    main()

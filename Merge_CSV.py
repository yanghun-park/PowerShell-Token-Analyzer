import csv, os, datetime

# ===== CSV Merger Program =====
# Merge all CSV files in the directory into one
# Final Amendment: 2020/09/16 (Version 1.0.0)
# Translation: 2021/04/29
# =========================

def main():
    FileName = "merged_normal.csv" # Files to Output
    TaskDir = "CSV_Files" # Tasks folder
    TaskPath = TaskDir + "\\"
    TaskList = os.listdir(TaskDir)
    
    print("---------- CSV Merge Tools ----------")
    print("* Caution: Initialize the existing generated file.")
    print("* File Name : " + FileName)
    print("--------------------------------------")
    first_time = datetime.datetime.now()

    CSV_Output = open(FileName, "w")
    CSV_OUT = [] # Create a Merge CSV Dictionary
    FileCount = 0
    FileMax = len(TaskList)

    for Name in TaskList:
        FileCount = FileCount + 1
        PATH = TaskPath + Name
        print("* Merging... - " + Name + " (" + str(FileCount) + "/" + str(FileMax) + ")")
        
        CSV_F = open(PATH, 'r') # CSV File Read
        CSV_Temp = CSV_F.readlines()
        for Line in CSV_Temp:
            Line = Line.rstrip() # Remove \n at the end of the sentence
            CSV_OUT.append(Line)


    print("* Generating final file...")
    for Line in CSV_OUT:
        CSV_Output.write(Line + '\n')

    CSV_Output.close()
    last_time = datetime.datetime.now()
    print("----------------------------")
    print("# Finish!")
    print("# Elapsed Time : " + str(last_time - first_time))
    print("----------------------------")
    return 0


if __name__ == '__main__':
    main()

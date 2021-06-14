# PowerShell-Token-Analyzer
## This program is designed to write a paper on powershell analysis.
- PSParser based Powershell token analysis program

* Name of thesis : Deep Learning Study on PowerShell Attack Detection Method (KIPS 2020.11) <br/>
* Link to thesis : http://kips.or.kr/bbs/confn/article/1490 <br/>

** The latest version : 1.9.15 (2020/09/23 updated) ** <br/>
** Translation into English : 2021/04/29 <br/>


### Recommand System
- Windows7 or later
- Python 3.7 or later

Before start, The module installation below is required. <br/>
- Revoke-Obfuscation : https://github.com/danielbohannon/Revoke-Obfuscation
- PSDecode : https://github.com/R3MRUM/PSDecode <br/>

### Start!
1. Open the editor and open file "Token_Analysis.py"
2. Change the parameter value in the main( ) function.
2. python Token_Analysis.py
3. Enter the number of files to partition
4. Please wait
5. Verify the generated csv file

### Tools
- Split_CSV.py : CSV splited program
- Merge_CSV.py : CSV merged program <br/>
@ Insert and run CSV file in CSV_Folder


<br/>Thanks!
<br/><br/>

---
### * Korean (한국어)

# PowerShell-Token-Analyzer (PowerShell 토큰 분석기)
## 이 프로그램은 PowerShell 토큰 분석에 관한 논문을 쓰기 위해 제작되었습니다. 
- PSParser 기반으로 한 파워쉘 분석 프로그램 입니다. 

* 관련 논문 : 파워쉘 공격 탐지방법에 대한 딥러닝 연구 (KIPS 2020.11) <br/>
* 링크 : http://kips.or.kr/bbs/confn/article/1490 <br/>

** 최종 업데이트 : 1.9.15 (2020/09/23 updated) ** <br/>

** 영어로 번역 : 2021/04/29 <br/>




### 권장 시스템
- Windows7 또는 그 이후버젼
- Python 3.7 또는 그 이후버젼

시작하기전에 아래의 모듈을 설치하시기 바랍니다.  <br/>
- Revoke-Obfuscation : https://github.com/danielbohannon/Revoke-Obfuscation
- PSDecode : https://github.com/R3MRUM/PSDecode <br/>

### 시작!
1. "Token_Analysis.py" 파일을 에디터로 엽니다. 
2. main() 함수의 파라미터 값을 변경합니다.  (파일 경로등...)
2. 아래와 같은 명령으로 실행합니다.  "python Token_Analysis.py"
3. 분할할 파일 수 입력후 엔터
4. 기다립니다.  (파일 개수 및 시퀀스 길이에 따라 소요되는 시간이 다릅니다.  )
5. 생성된 CSV 파일을 확인합니다. 

### 도구 모음
- Split_CSV.py : CSV 분활 프로그램
- Merge_CSV.py : CSV 병합 프로그램 <br/>
@ CSV 폴더를 생성 후 병합할 CSV 파일들을 넣습니다. 

<br/>

감사합니다. 



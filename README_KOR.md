# PowerShell-Token-Analyzer (PowerShell 토큰 분석기)
## 이 프로그램은 PowerShell 토큰 분석에 관한 논문을 쓰기 위해 제작되었습니다. 
- PSParser 기반으로 한 파워쉘 분석 프로그램 입니다. 

* 관련 논문 : 명령 실행 모니터링과 딥 러닝을 이용한 파워셸 기반 악성코드 탐지 방법 (KIPS 2020.11) <br/>
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




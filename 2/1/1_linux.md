# 수행 목표
실습을 위한 ubuntu 환경을 구성한다.

# ROS2 학습을 위한 리눅스 운영체제 사용법 학습
## 1.셀 환경이 실행되는 터미널 실행 방법
 - 터미널(Terminal)은 리눅스에서 명령어를 입력하는 창이고, 셸(Shell)은 이 터미널에서 동작하는 프로그램이다.
 - 우분투에서 **단축키 [Ctrl+Alt+T]를 사용하여 터미널을 실행**할 수 있다.

## 2.파일과 디렉토리를 관리하는데 필요한 명령어
 - **pwd**: 현재 디렉토리 경로 표시

 - **touch (파일명)**: 빈 파일 생성

 - **rmdir (폴더명)**: 빈 디렉토리 삭제

 - **file (파일명)**: 파일 타입 확인

 - **ls**
     - **ls**: 폴더에 들어있는 파일 목록
     - **ls -i**: 파일의 상세 정보(권한, 크기 등)
     - **ls -a**: 숨김 파일 포함 정보(숨김 파일은 .으로 시작)

 - **cd**
     - **cd**: 해당 디렉토리로 이동
     - **cd..**: 상위 디렉토리로 이동(이전 폴더로 이동)

 - **mkdir**
     - **mkdir (폴더명)**: (폴더명)이름의 새 폴더 생성
     - **mkdir -p (경로/중간/최종)**: 중간 디렉토리까지 한번에 생성 

 - **cp**
     - **cp (원본 대상)**: (원본 대상)파일 복사
     - **cp -r (원본폴더) (대상폴더)**: 디렉토리 복사
     - **cp -i (파일1) (파일2)**: 덮어쓰기 전 확인
     - **cp -u (파일1) (파일2)**: 대상보다 최신인 경우에만 복사
    
 - **mv**
     - **mv (파일이름) (새이름)**: 파일/폴더 이름 변경
     - **mv (대상폴더/)**: 다른 위치로 이동

 - **rm**
     - **rm (파일명)**: 파일 삭제
     - **rm -i (파일명)**: 삭제 전 확인
     - **rm -r (폴더명)**: 폴더 및 내부 내용 삭제
     - **rm -rf 디렉토리명**: 강제 삭제 (복구 불가)

 - **find**
     - **find (. or /) -name "(파일이나 폴더 이름)"**: 이름으로 검색
     - **find . -name "*.txt"**: 현재 디렉토리(.) 이하에서 이름이 .txt로 끝나는 파일 검색
     - **find / -type d -iname "(파일이나 폴더 이름)"**: /루트 디렉토리부터 전체 경로를 검색, 디렉토리만 검색(-type d), 대소문자 무시하고 찾기(-iname)

## 3.파일의 내용을 확인하고 편집하는 방법
 - **cat (파일명)**: 파일 내용을 한 번에 출력

 - **less (파일명)**: 페이지 단위로 위아래 스크롤 가능(q로 종료)

 - **more (파일명)**: 페이지 단위로 아래로만 스크롤 가능(q로 종료)

 - **head -n 10 (파일명)**: 파일 내용 앞의 10줄 출력

 - **tail -n 10 (파일명)**: 파일 내용 뒤의 10줄 출력

 - **nano (파일명)**: 간단한 텍스트 편집기(파일 편집)

 - **vim (파일명)**: 고급 텍스트 편집기(nano에 비해 사용하기 어렵다.)

## 4.파일의 권한에 대한 개념과 파일의 권한을 바꾸는 방법
### 4-1. 리눅스 파일 권한
 - **r(read)**: 읽기
 - **w(write)**: 쓰기
 - **x(execure)**: 실행
 - 각 파일은 소유자, 그룹, 다른 사용자에 대한 권한을 설정할 수 있다.
 - ls -i를 사용하여 파일에 대한 권한을 확인할 수 있다.

### 4-2. 권한 변경
 - **chmod**
     - **chmod +x (파일명)**: 실행 권한 추가
     - **chmod 755 (파일명)**: 숫자로 권한 설정
 - **chown**
     - **chown (사용자) (파일명)**: 파일 소유자 변경
     - **chown (사용자:그룹 파일명)**: 소유자와 그룹 동시에 변경

## 5.실행파일, 셸 스크립트의 개념과 source 명령어 사용법
### 5-1. 실행파일
 - 컴퓨터가 직접 실행할 수 있는 프로그램 파일
 - 보통 C/C++, Python 등을 컴파일하거나 빌드했을 때 생성된다.
 - .sh 같은 스크립트 파일에 실행 권한(chmod +x)을 주면 실행파일처럼 동작할 수 있다.
### 5-2. 셸 스크립트
 - 리눅스 명령어들을 모아놓은 텍스트 파일이다.
 - .sh 확장자를 주로 사용하며, 셸(예: bash)이 이 파일을 위에서부터 한 줄씩 실행한다.
### 5-3. source 명령어
 - 셸 스크립트를 실행하되, 현재 셸 환경에서 실행하고 싶을 때 사용한다.
 - 스크립트 내용을 현재 터미널 환경에서 실행한다.
 - source는 새로운 셸을 만들지 않고 지금 터미널에 그대로 반영한다.


## 6.사용자 권한, 슈퍼유저의 개념과 sudo 명령어
### 6-1. 사용자와 권한의 개념
 - 리눅스에서 모든 파일과 프로세스는 소유자가 있다.
     - 각각의 파일은 소유자, 그룹, 기타 사용자로 나뉜다.
     - 각 사용자에 대해 **읽기(r), 쓰기(w), 실행(x) 권한**이 따로 설졍된다.

### 6-2. 일반 사용자, 슈퍼유저(root)
 - 일반 사용자는 시스템의 파일 수정, 패키지 설치, 서비스 제어등이 제한된다.

 - root사용자는 시스템에서 최고 권한을 가진 관리자 이다.
     - 모든 파일, 디렉토리, 명령어 실행, 시스템 설정 변경이 가능하다.
### 6-3. sudo(superuser do) 명령어
 - sudo를 사용하여 일반 사용자가 일시적으로 root권한을 얻어 명령을 실행할 수 있다.
 - 사용 예: 
     - sudo cp ./myfile /etc/myconfig/ (시스템 디렉토리에 파일 복사)
     - sudo chmod 755 /usr/bin/myscript (파일 권한 변경)

## 7.우분투 리눅스의 패키지 관리 방법과 apt 명령어
### 7-1. 패키지
 - 패키지(Package)
     - 프로그램, 라이브러리, 설정 파일 등을 하나로 묶은 배포 단위이다.
     - .deb 확장자를 가진 파일

 - 패키지 관리자
     - 설치, 업데이트, 삭제, 의존성 관리 등을 자동으로 해주는 툴
     - 우분투는 APT(Advanced Package Tool)로 소프트웨어를 관리한다.
### 7-2. APT
 - **apt는 우분투에서 패키지를 설치/삭제/업데이트할 수 있는 명령어**이다.
 - 내부적으로는 /etc/apt/sources.list 파일에 명시된 저장소(repository) 에서 패키지를 받아온다.
 - **sudo apt update**: 저장소에서 최신 패키지 목록을 가져온다.

 - **sudo apt upgrade**: 현재 설치된 패키지를 최신 버전으로 업그레이드

 - **sudo apt install (패키지명)**: 새로운 패키지를 설치

 - **sudo apt remove (패키지명)**: 패키지를 삭제하되, 설정파일은 보존

 - **sudo apt purge (패키지명)**:	패키지 삭제 + 설정파일까지 제거

 - **sudo apt autoremove**:	더 이상 사용되지 않는 의존성 패키지 제거

 - **sudo apt clean**: 다운로드한 패키지 캐시 삭제 (/var/cache/apt/archives)

 - **apt list --installed**: 설치된 모든 패키지 목록 보기

 - **apt search (이름)**:	패키지 이름으로 검색

 - **apt show (이름)**:	패키지 상세 정보 보기

## 8.홈 디렉토리의 개념
### 홈 디렉토리
 - 홈 디렉토리(/home/사용자명)는 각 사용자별 작업 공간이다.
 - 개인 파일, 설정, 다운로드파일 등이 저장된다.
 - ~ 기호는 홈 디렉토리를 의미한다. (cd ~: 홈으로 이동, cd ~/Documents: 홈에서 Documents로 이동)
 - 주요 디렉토리
     - **~/Documents**: 문서 저장용

     - **~/Downloads**: 다운로드 파일

     - **~/ros2_ws**: ROS2 작업 공간을 보통 여기에 생성한다.

 - 숨김 설정 파일 및 폴더(.으로 시작한다.)
    - **~/.bashrc**: 터미널에서 Bash 셸 환경 설정 (alias, PATH 등)

    - **~/.profile**: 로그인 시 실행되는 환경설정 (bash 외에도 적용)

    - **~/.bash_history**:	사용한 명령어 기록

    - **~/.config/**: 다양한 프로그램 설정 파일 저장 (예: VSCode, Qt, ROS 등)

    - **~/.local/**: 사용자 설치 프로그램, 파이썬 패키지 등 저장

    - **~/.cache/**: 프로그램의 임시 캐시 데이터 저장

    - **~/.ssh/**:	SSH 키, known_hosts 등 원격 접속 관련 설정

    - **~/.gitconfig**: Git 사용자 설정 저장 (전역 설정)

#  Chrome, VS code 설치 및 Python 파일 실행
## 1. chrome, VScode 설치 및 실행
### 1-1. chrome 브라우저 설치
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb  
sudo apt install ./google-chrome-stable_current_amd64.deb -y  

google-chrome # chrome 창 실행

### 1-2. VScode 설치
sudo apt install software-properties-common apt-transport-https -y  
wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | sudo apt-key add -  
sudo add-apt-repository "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main"  
sudo apt update  
sudo apt install code -y  

code # 설치된 VS code 실행

## 2. ~/study/linux 디렉토리에 간단한 파이썬 프로그램을 작성 및 실행
### 2-1. 디렉토리 생성
**mkdir -p ~/study/linux**  
### 2-2. VS code로 파일 열기
**code /home/genie/study/linux/1_hello.py**  
### 2-3. 터미널에서 Python파일 실행
**python3 ~/study/linux/1_hello.py**  
     - 출력: Permission denied: 관리자 권한이 필요합니다.
     - **/test는 리눅스 루트 디렉토리 언어**이기 때문에 일반 사용자로는 사용할 수 없다.
### 2-4. sudo로 실행하여 권한 문제를 해결하여 예외 없이 실행되도록 한다.
**sudo python3 ~/study/linux/1_hello.py**  
     - 출력: [sudo] password for genie: 
     - 출력: 파일 생성 완료!
### 2-5. 파일 내용 확인
**ls -l /test  # 파일 존재 확인**   
     - 출력: total 4  
     - 출력: -rw-r--r-- 1 root root 11  5월 19 21:22 hello.txt  
**cat /test/hello.txt  # 파일 내용 확인**   
     - 출력: Hello Linux

## 3. 질문
### 확인하기 쉬운 홈 디렉토리가 아니라 루트 디렉토리 아래에 /test같은 디렉토리를 만드는 이유가 뭔지 알고싶다.
 - **ls -/, ls -l /, ls -la /**를 사용하여 루트 디렉토리 아래에 있는 파일도 확인 가능하다.
 - 시스템 전체 공유 필요
     - 사용자 계정과 무관하게 접근 가능한 디렉토리가 필요할 때
 - 홈 디렉토리 보호
     - 사용자 파일과 분리해서 실험하고 싶을 때
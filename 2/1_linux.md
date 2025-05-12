# 수행 목표
- 실습을 위한 ubuntu 환경을 구성한다.

# ROS2 학습을 위한 리눅스 운영체제 사용법 학습
## 1.셀 환경이 실행되는 터미널 실행 방법
 - 터미널(Terminal)은 리눅스에서 명령어를 입력하는 창이고, 셸(Shell)은 이 터미널에서 동작하는 프로그램이다.
 - 우분투에서 단축키 [Ctrl+Alt+T]를 사용하여 터미널을 실행할 수 있다.

## 2.파일과 디렉토리를 관리하는데 필요한 명령어
 - **pwd**: 현재 디렉토리 경로 표시
 - **ls / ls -i / ls -a**: 폴더에 들어있는 파일 목록 / 파일의 자세한 정보 / 숨김 파일 포함 정보
 - **cd / cd..**: 해당 디렉토리로 이동 / 상위 디렉토리로 이동(이전 폴더로 이동)
 - **mkdir (폴더명)**: (폴더명)이름의 새 폴더 생성
 - **cp (원본 대상)**: (원본 대상)파일 복사
 - **mv (원본 대상)**: 파일/폴더 이름 변경 또는 이동
 - **rm (파일명) / rm -r (폴더명)**: 파일 삭제 / 폴더와 그 안의 내용 삭제

## 3.파일의 내용을 확인하고 편집하는 방법
 - **cat (파일명)**: 파일 내용 전체 출력
 - **less (파일명), more (파일명)**: 페이지 단위로 파일 내용 출력(위아래로 스크롤 가능)
 - **head -n 10 (파일명)**: 파일 내용 앞의 10줄 보기
 - **tail -n 10 (파일명)**: 파일 내용 뒤의 10줄 보기
 - **nano (파일명)**: 간단한 텍스트 편집기(파일 편집)
 - **vim (파일명)**: 고급 텍스트 편집기(nano에 비해 사용하기 어렵다.)

## 4.파일의 권한에 대한 개념과 파일의 권한을 바꾸는 방법
### 리눅스 파일 권한
 - **r(read)**: 읽기
 - **w(write)**: 쓰기
 - **x(execure)**: 실행
 - 각 파일은 소유자, 그룹, 다른 사용자에 대한 권한을 설정할 수 있다.
 - ls -i를 사용하여 파일에 대한 권한을 확인할 수 있다.
### 권한 변경
 - **chmod +x (파일명)**: 실행 권한 추가
 - **chmod 755 (파일명)**: 숫자로 권한 설정

## 5.실행파일, 셸 스크립트의 개념과 source 명령어 사용법
### 실행파일
 - 컴퓨터가 직접 실행할 수 있는 프로그램 파일
 - 보통 C/C++, Python 등을 컴파일하거나 빌드했을 때 생성된다.
 - .sh 같은 스크립트 파일에 실행 권한(chmod +x)을 주면 실행파일처럼 동작할 수 있다.
### 셸 스크립트
 - 리눅스 명령어들을 모아놓은 텍스트 파일이다.
 - .sh 확장자를 주로 사용하며, 셸(예: bash)이 이 파일을 위에서부터 한 줄씩 실행한다.
### source 명령어
 - 스크립트 내용을 현재 터미널 환경에서 실행한다.
 - source는 새로운 셸을 만들지 않고 지금 터미널에 그대로 반영한다.


## 6.사용자 권한, 슈퍼유저의 개념과 sudo 명령어
 - **일반 사용자**는 시스템 파일 변경 권한이 없다.
 - **슈퍼유저(root)**는 모든 권한을 가진 관리자이다.
 - sudo (명령어): sudo를 사용하여 일시적으로 root권한을 얻어 명령을 실행할 수 있다.
 - 사용 예: sudo apt update, sudo nano /etc/hosts등

## 7.우분투 리눅스의 패키지 관리 방법과 apt 명령어
 - 우분투는 APT(Advanced Package Tool)로 소프트웨어를 관리한다.
 - **sudo apt update**: 패키지 목록 업데이트
 - **sudo apt upgrade**: 패키지 업그레이드
 - **sudo apt install (패키지명)**: 프로그램 설치
 - **sudo apt remove (패키지명)**: 프로그램 제거
 - **apt search (키워드)**: 패키지 검색

## 8.홈 디렉토리의 개념
### 홈 디렉토리
 - 홈 디렉토리(/home/사용자명)는 사용자별 작업 공간이다.
 - 개인 파일, 설정, 다운로드파일 등이 저장된다.
 - ~ 기호는 홈 디렉토리를 의미한다. (cd ~: 홈으로 이동, cd ~/Documents: 홈에서 Documents로 이동)
### 주요 디렉토리
 - **~/Documents**: 문서 저장용
 - **~/Downloads**: 다운로드 파일
 - **~/.bashrc, ~/.profile**: 사용자 환경설정 파일
 - **~/ros2_ws**: ROS2 작업 공간을 보통 여기에 생성한다.

# chrome, VScode 설치 및 실행
## 1. chrome 브라우저 설치
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb  
sudo apt install ./google-chrome-stable_current_amd64.deb -y  

## 2. VScode 설치
sudo apt install software-properties-common apt-transport-https -y  
wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | sudo apt-key add -  
sudo add-apt-repository "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main"  
sudo apt update  
sudo apt install code -y  


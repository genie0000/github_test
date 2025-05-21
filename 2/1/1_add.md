# 참고 영상
https://www.youtube.com/watch?v=oBfqiUhbsRw

## 업데이트하기
sudo apt-get update
sudo apt-get upgrade
한글 설정을 하고나서 폴더이름은 한글로 업데이트 하지 않아야 한다.

## 터미네이터 설치(창 나눌 때 효율적이다.)
sudo apt update
sudo apt install terminator

## 크롬 설치
wget --version  # 만약 버전이 없으면 -->   
sudo apt update  
sudo apt install wget  

## 우분투 버전 업그레이드 알림 완전히 끄는 방법
sudo nano /etc/update-manager/release-upgrades  
1. 아래 부분을 찾는다.
Prompt=lts  
2. 이걸 다음처럼 변경한다.
Prompt=never  
3. 저장 방법
Ctrl + O → 엔터 (저장)  
Ctrl + X (종료)

## 깃허브 설치
git --version  # 만약 버전이 없으면 -->  
sudo apt update  
sudo apt install git  

## 코드에서 한국어 변환이 안될 때
sudo snap remove code  # https://code.visualstudio.com/download 여기서 deb코드 설치  
sudo dpkg -i code_1.40.2-1574694120_amd64.deb  # 다운로드 폴더 내에서 dpkg 해야한다.  
sudo apt -f install  # 만약 설치 중 의존 라이브러리가 없다는 메시지가 나오면 실행한다.  
hash -r  # 만약 code로 안열리면 쉘 해시 초기화를 해본다.  

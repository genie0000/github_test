# 수행 목표
ROS2에 대한 조사 및 ROS2 활용 실습 환경을 구성한다.
ros2 run 명령의 사용법을 학습한다.

# ROS2 학습
## 1. 로봇 운영체제의 개념
### 1-1. ROS 정의
 - 로봇 운영체제(ROS)는 Robot Operating System으로 로봇 소프트웨어 개발을 위한 오픈 소스 프레임워크 이다.
 - 운영체제라기 보다는 로봇 소프트웨어를 쉽게 개발하고 연결할 수 있도록 도와주는 툴 모음이다.
### 1-2. 사용 목적
 - 로봇을 모듈화된 구조로 개발하고, 복잡한 로봇 시스템을 효율적으로 통합 및 제어할 수 있다.
 - 여러 센서, 액추에이터, 알고리즘 등을 분산된 노드(Node)로 연결하기 위해 사용한다.
### 1-3. 주요 기능
 - 통신: 노드 간 메시지 송수신, 서비스 호출, 액션 통신 등
 - 패키지: 소프트웨어를 패키지 단위로 구성하여 배포 및 재사용 가능
 - 시뮬레이션: Gazebo등과 연동하여 가상 환경 테스트 가능
 - 시각화 도구: Rviz등을 통해 로봇 상태, 센서 정보 시각화 가능
### 1-4. ROS 구조의 핵심 개념
 - Node: 하나의 기능을 수행하는 독립적으로 실행하는 단위의 프로그램
     - 예: 센서 입력 노드, 제어 노드 등
 - Topic: 노드 간 비동기 메시지 통신 채널
 - Publisher/Subscriber: 정보를 보내는 노드/ 정보를 받는 노드

## 2. 운영 체제를 사용해 동작하는 로봇과 그렇지 않는 로봇의 차이 조사
 - 운영체제를 사용하는 로봇은 복잡한 작업을 동시에 수행할 수 있고, 유지보수 및 확장성이 뛰어나다.
### 2-1. 운영 체제를 사용하는 로봇
 - linux 같은 일반 운영체제나 RTOS(실시간 운영체제)를 탑재한 로봇, ROS2(미들웨어)도 이런 OS 위에서 동작한다.
    - 복잡한 작업 가능 (AI, SLAM, 이미지처리 등)
    - 멀티태스킹이 가능하다.
    - 시스템 구조가 복잡하지만 유연성이 높다. (ROS)
    - 실시간성이 일반 OS는 낮지만 RTOS는 높다.
    - 로그, 쉘, 시각화 툴을 사용하여 여러 정보를 다양하게 확인할 수 있다.
### 2-2. 운영 체제를 사용하지 않는 로봇
 - MCU에 임베디드 코드를 올려 동작하고, OS없이 전용 제어 루틴만 있다.
     - 단순 제어만 가능 (LED, 모터 ON/OFF 등)
     - 멀티태스킹이 제한적이다.
     - 시스템 구조가 단순하고, 하드코딩 중심이다.
     - 실시간성 확보가 가능하다.
     - UART등으로 제한적으로 정보를 확인할 수 있다.

## 3. 우분투 리눅스에 ROS2를 설치하는 방법 조사 및 humble 배포폰 설치
 - https://docs.ros.org/en/humble/ # humble 공식 홈페이지에서 설치 진행
 - Set locale
     - locale
     - sudo apt update && sudo apt install locales
     - sudo locale-gen en_US en_US.UTF-8
     - sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
     - export LANG=en_US.UTF-8
     - locale  # verify settings
 - Setup Sources
     - sudo apt install software-properties-common
     - sudo add-apt-repository universe
     - sudo apt update && sudo apt install curl -y
     - sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
     - echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
 - 설치 확인
     - ls /etc/apt/sources.list.d/  # ros2.list가 있는 것을 확인할 수 있다.
 - Install ROS 2 packages
     - sudo apt update
     - sudo apt upgrade
     - sudo apt install ros-humble-desktop
 - 설치 확인
     - ls /opt/ros/humble/

## 4. ROS2로 동작하는 제어 프로그램에서 패키지와 노드의 관계
 - 패키지는 하나 이상의 노드를 포함할 수 있다.
 - 노드는 반드시 패키지 안에 있어야 ROS2가 인식하고 실행할 수 있다.
### 4-1. 패키지(Package)
 - ROS2에서 기능 단위로 코드를 묶는 기본 단위
 - 라이브러리, 노드, 메시지, launch 파일 등 포함
### 4-2. 노드(Node)
 - 패키지 안에 있는 실행 가능한 프로그램(프로세스)
 - 센서 데이터 읽기, 제어 명령 전송 등의 역할 수행

## 5. ros2 run 명령의 사용법
 - ros2 run 명령은 ROS2 패키지 안의 실행 가능한 노드를 실행할 때 사용하는 명령어이다.
 - ros2 run (패키지 이름) (실행파일 이름)

## 6. 두 개의 터미널을 실행하고, 각각의 터미널에서 두 개의 데모 프로그램을 동시에 실행
### ROS2를 사용하려면 터미널을 열 때마다 아래 명령을 실행해야 한다.
 - source /opt/ros/humble/setup.bash
### 6-1. demo_nodes_cpp 패키지의 talker 노드 실행
 - ros2 run demo_nodes_cpp talker
### 6-2. demo_nodes_cpp 패키지의 listener 노드 실행
 - ros2 run demo_nodes_cpp listener

### 6-3. 두 개의 노드는 동시에 실행되고, 서로 상호작용하는지 확인

### 6-4. 이를 실행하기 위해서 환경 설정과 관련된 어떤 추가 작업이 필요한지 확인한다. 이 과정을 거쳐 두 개의 데모 프로그램을 실행한 후, 프로그램의 결과를 확인한다.


### 6-5. 데모 프로그램의 실행 화면을 캡쳐해 이미지 파일로 저장한다. 동시에 실행되어 상호작용하고 있는 상황을 확인할 수 있는 이미지를 저장해야 한다.




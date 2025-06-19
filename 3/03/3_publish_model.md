# 수행목표
로봇의 상태를 게시하는 방법을 확인하고, 로봇 상태 퍼블리셔를 구현한다.

## 1. ROS2에서 로봇의 상태를 게시한다는 것의 의미는 무엇인지 조사한다.
### 1-1. 로봇의 상태란
 - 로봇이 현재 어떤 위치에 있고, 어떻게 움직이고 있으며, 각 부위(관절, 바퀴, 센서 등)의 상태가 어떤지를 나타내는 정보를 의미한다.
     - 예시: 로봇의 위치(x, t, θ), 바퀴의 회전 속도, 관절의 각도, 배터리 잔량, 센서의 측정값(온도, 거리, 충돌 여부 등)

### 1-2. 로봇의 상태를 게시(publish)한다는 것의 의미
 - 로봇 내부의 정보를 주기적으로 측정하여 특정 토픽에 메시지 현태로 보내는 것
     - 예시: /joint_states 토픽에 로봇의 관절 위치, 속도, 토크 등을 게시 (주로 sensor_msgs/msg/JointState 메시지 타입 사용)
     - /odom 토픽에 로봇의 위치/방향 등 주행 상태를 게시 (주로 nav_msgs/msg/Odometry 메시지 타입 사용)
     - /tf 또는 /tf_static 프레임에 좌표계 관계 정보를 게시 (tf2를 통해 로봇의 각 링크 위치 등을 시각화 가능)

- 로봇 하드웨어/시뮬레이터 --> State Publisher 노드(센서 or joint 정보 측정) --> /joint_states 토픽에 메시지 게시 --> RViz2/Controller 노드(정보를 받아서 표시하거나 제어)

## 2. URDF로 정의된 로봇의 상태를 게시하는 방법을 조사한다.(robot_state_publisher 노드와 /joint_states 메시지의 관계를 중심으로 조사)
 - URDF + /joint_staes --> robot_state_publisher 노드 --> /tf 토픽에 링크들 위치를 게시 --> RViz2, SLAM, 제어기 등에서 로봇 자세 인식 가능

### 2-1. 구조
 - URDF: 로봇의 물리 구조(링크, 조인트 등)를 정의
 - /joint_states 토픽: 로봇의 관절 위치(각도, 속도 등)를 주기적으로 전달하는 메시지
 - robot_state_publisher 노드: URDF + /joint_states → 링크 간 상대 위치(TF)로 변환해 게시
### 2-2. /joint_states 메시지
 - ROS 2에서 sensor_msgs/msg/JointState 메시지 형식을 사용한다.
### 2-3. robot_state_publisher 노드의 역할
 - URDF파일과 /joint_states메시지를 입력받음
 - 각 조인트의 현재 각도를 바탕으로 링크 간 위치/자세 계산
 - /tf 또는 /rf_static 토픽에 로봇 각 링크의 좌표계 관계 게시(RViz2 등에서 로봇의 현재 자세를 시각화 가능)

## 3. 이전 문제에서 만든 간단한 로봇 모델의 조인트 상태를 게시하는 노드를 파이썬 프로그램으로 구현한다. joint_state_publisher.py 파일에 작성한다.
1. 이 파이썬 프로그램은 /joint_states 토픽에 상태를 게시한다.
2. robot_state_publisher 노드와 함께 실행해 RViz2에서 로봇의 모델을 확인할 수 있어야 한다.

 - /joint_states 토픽에 조인트 상태를 게시하는 파이썬 노드 구현
 - 이전에 만든 URDF 사용
 - robot_state_publisher와 03_joint_state_publisher.py 노드, RViz2를 함께 실행
 - 메시지 타입은 sensor_msgs.msg.JointState 이다.

## 4. Launch File을 작성한다. 실행하면 작성한 모델 파일 및 노드를 사용해 RViz2에서 로봇 모델을 확인할 수 있어야 한다.
1. setup.py, package.xml 파일도 필요한 경우 작성하거나 수정한다.
2. Launch File에는 RViz 설정 파일과 관련된 사항을 추가한다.

 - 런치파일 실행
    - source install/setup.bash
    - ros2 launch my_robot_controller3 publish_state_launch.py 

 - 오류 발생 
     - base_link  
     No transform from [base_link] to [map]      
     left_wheel  
     No transform from [left_wheel] to [map]    
     right_wheel  
     No transform from [right_wheel] to [map]  
- map 프레임과 base_link 프레임 사이에 TF가 없음
- 로봇 상태 퍼블리셔(robot_state_publisher)는 base_link부터 로봇 링크들의 TF를 게시한다.
- 하지만 map 프레임과 로봇 프레임(base_link) 사이를 연결하는 TF는 별도의 노드에서 발행해야 한다. (예: amcl 노드, slam_toolbox 노드, 또는 static_transform_publisher)

 - 임시로 고정 TF 연결 추가
    - ros2 run tf2_ros static_transform_publisher 0 0 0 0 0 0 map base_link

## 5. 실행해서 결과를 확인한다.
1. RViz2에서 RViz 설정 파일을 저장한다.

## 6. 조사한 내용을 형식 문서로 만들고 워크 스페이스 디렉토리를 압축해 함께 게시한다.

프로젝트 루트의 3/3 디렉토리를 생성한 후, 이 디렉토리 내에 문서 파일의 이름은 3_publish_model.md(마크다운 파일의 경우)으로 저장, 게시한다.
# 수행목표
Gazebo 시뮬레이터에서 환경(World)를 만든다.

## 1. Gazebo 시뮬레이터의 환경 파일에 대해서 조사한다.
### 1-1. Gazebo 시뮬레이터 환경 파일
 - Gazebo에서 말하는 환경(Environment)은 로봇이 시뮬레이션되는 월드(World)를 의미한다.
 - .world 파일은 XML 기반의 SDF(Simulation Description Format) 형식으로 작성된다.
### 1-2. 환경 파일 태그 정리
 - `<include>`  외부 모델 또는 요소 불러오기 (model://)
 - `<physics>`	시뮬레이션 물리 엔진 설정
 - `<light>`	광원 추가 (태양, 조명 등)
 - `<model>`	직접 모델을 정의할 수도 있음
 - `<gui>`	    GUI 시점, 카메라 위치 등 조정

## 2. Gazebo 시뮬레이션 환경을 작성하는 방법에 대해서 조사한다.
### 2-1. 텍스트 에디터로 직접 .world 파일 작성 (SDF 방식)
 - .world 파일은 XML 기반의 SDF(Simulation Description Format) 형식으로 작성
### 2-2. Gazebo GUI 내에서 직접 편집
 - Gazebo 실행 후 --> 왼쪽 모델 리스트에서 끌어다 놓고 배치
 - 원하는 위치에 모델을 놓고 회전/이동/크기 조절
 - 최종적으로 메뉴 → File → Save As → .world로 저장 가능
### 2-3. 기존 모델들을 조합하여 환경 구성 (model:// 사용)
- 기존 Gazebo 모델 라이브러리를 재활용 가능
### 2-4. ROS 2 패키지와 연동된 Launch 파일에서 지정
- ROS 패키지와 통합 관리 가능
### 2-5. Blender 또는 외부 3D 툴로 모델 제작 후 불러오기
- .dae, .obj, .stl 등의 3D 모델을 Gazebo에 불러올 수 있다.
- 충돌(collision)이나 물리엔진 세부 설정은 따로 지정 필요

## 3. 월드 좌표계와 로컬 좌표계에 대해서 조사한다.
### 3-1. 월드 좌표계 (World Coordinate System)
 - 시뮬레이션 전체의 기준이 되는 좌표계이다. (절대 위치)
 - 보통 (0, 0, 0)은 지면의 중심 또는 월드의 원점
 - 기준 축
    - X: 앞 방향 (East)
    - Y : 왼쪽 방향 (North)
    - Z: 위 방향 (Up)
### 3-2. 로컬 좌표계 (Local Coordinate System)
 - 각 오브젝트(로봇, 센서, 링크 등) 자체에 종속된 좌표계이다. (상대 위치)
 - 기준은 해당 오브젝트의 중심 또는 기준 지점
 - 보통 로봇 기준의 base_link, 링크 기준 link_name, 센서 기준의 sensor_link 등이 있다.
 - 로봇의 앞 방향은 보통 +X, 위쪽은 +Z, 왼쪽은 +Y이다.
### 3-3. 두 좌표계의 관계
- 로컬 좌표계는 월드 좌표계를 기준으로 변환(transform)되고,
- 이때 사용되는 정보가 Pose (position + orientation)이다.

## 4. 환경 파일과 함께 시뮬레이터를 실행하는 방법을 조사한다.
 - 환경파일 실행
 - gazebo my_world.world
 - ros2 launch gazebo_ros gazebo.launch.py world:=/path/to/your_world.world

## 5. 다음과 같이 시뮬레이션이 가능하도록 이전 문제의 결과물을 수정한다.
1. 평탄한 바닥에 적당한 크기의 원형 경로를 가진 환경(World)을 생성한다. 원형 경로의 크기는 이전 문제에서 만든 로봇이 그리는 원의 크기와 동일하도록 한다.
2. 시뮬레이션 환경에서 로봇이 경로 위에서 원을 그리며 돌도록 로봇을 배치한다. 로봇의 초기 위치 및 초기 방향은 제어노드에 지정하며, 시뮬레이터 상의 배치 결과 및 원형 주행 결과를 확인하면서 값을 조정한다.
3. 시뮬레이션이 시작되면 시뮬레이션 환경에서 로봇이 경로를 따라 도는 시뮬레이션을 시작하고, 사용자가 중단시킬 때 까지 이를 반복하도록 Launch File 및 기타 필요한 파일을 수정한다.

 - Gazebo만 실행 + 원하는 월드 로드
gazebo /절대경로/your_world.world
gazebo ~/ros2_ws/src/my_robot_controller3/worlds/circular_track.world
- Gazebo + ROS2 통합 실행
ros2 launch gazebo_ros gazebo.launch.py world:=/절대경로/your_world.world
ros2 launch gazebo_ros gazebo.launch.py world:=~/ros2_ws3/src/my_robot_controller3/worlds/circular_track.world 

ros2 launch gazebo_ros gazebo.launch.py world:=~/ros2_ws/src/my_robot_controller3/worlds/circular_track.world

- 로봇 스폰
ros2 run gazebo_ros spawn_entity.py \
  -entity my_robot \
  -file ~/ros2_ws/src/my_robot_controller3/urdf/simple_wheel_robot.urdf \
  -x 0 -y 0 -z 0.1



## 빌드, 실행 후 결과를 확인한다.
조사한 내용을 형식 문서로 만들고 워크 스페이스 디렉토리를 압축해 함께 게시한다.
프로젝트 루트의 3/6 디렉토리를 생성한 후, 이 디렉토리 내에 문서 파일의 이름은 6_gazebo_world.md(마크다운 파일의 경우)으로 저장, 게시한다.
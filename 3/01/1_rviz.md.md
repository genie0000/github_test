# 수행목표
RViz2 사용법에 대해서 알아본다.
TF(Transform Frames)에 대해서 알아본다.

# RViz2 및 TF 학습
## 1. ros-humble-urdf-tutorial 패키지를 설치한다.
 - sudo apt install ros-humble-urdf-tutorial

## 2. 다음 명령을 실행해보자. RViz 프로그램이 실행되어야 한다.
 - ros2 launch urdf_tutorial display.launch.py model:=/opt/ros/humble/share/urdf_tutorial/urdf/08-macroed.urdf.xacro

## 3. RViz2가 보여주는 로봇을 다양한 방식으로 확인해보자.
1. Displays > RobotModels > Links의 여러 항목의 일부를 선택 / 비선택 하면서 로봇 모델이 어떤 구조로 되어 있는지를 확인해본다.
2. 여러 옵션 옵션들도 변경 가능한 값을 수정하면서 RViz2가 보여주는 로봇의 형태를 바꿔본다.

## 4. TF에 대해서 조사한다.
### 4-1. TF의 주요 세 가지 개념인 좌표계, 변환, 트리에 대해서 조사한다.
**TF(Transform Frames)는 ROS에서 여러 로봇 부품이나 센서, 환경 객체 등 다양한 요소들의 3D 자세를 시간 경과에 따라 추적하고 관리하는 시스템이며 좌표계, 변환, 트리로 구성되어있다.**
 - **좌표계(Coordinate Frame)**
     - **3D 공간에서 특정 지점의 위치와 방향을 나타내기 위한 기준 틀이다.**
     - 각 로봇의 부품이나 환경 내의 특정 지점은 고유한 좌표계를 가진다.
     - 예를 들어, base_link는 로봇의 기준이 되는 좌표계이고, gripper_link는 로봇 팔의 그리퍼 끝단의 좌표계가 될 수 있고, 모든 좌표계는 이름으로 식별된다.
 - **변환(Transform)**
     - **한 좌표계에서 다른 좌표계로 위치와 방향 정보를 변환하는 과정이다.**
     - 주로 변환 행렬(Transformation Matrix) 또는 쿼터니언(Quaternion)과 벡터(Vector) 조합으로 표현된다.
     -  예를 들어, base_link 좌표계에서 gripper_link 좌표계로의 변환은 로봇 몸체 기준으로 그리퍼가 어디에 있고 어떤 방향을 향하는지를 알려준다.
 - **트리(Transform Tree)**
     - **모든 좌표계와 그들 간 변환 관계를 계층적으로 연결한 구조이다.**
     - 하나의 부모(parent)좌표계에 여러 자식(child)좌표계가 연결될 수 있다.
     - 모든 변환은 이 트리 구조를 따라 이루어진다.
     - **TF는 이 트리를 사용하여 어떤 두 좌표계 사이의 변환이라도 계산할 수 있도록 한다.**
     - 예를 들어, world 좌표계에서 camera_link 좌표계까지의 변환을 알고 싶다면, TF는 world에서 base_link로, base_link에서 robot_arm으로, robot_arm에서 camera_link로 이어지는 변환들을 조합하여 최종 변환을 계산한다.

### 4-2. RViz2에서 좌표계, 변환, 트리를 확인하는 방법을 찾는다.
**RViz2는 TF 정보를 시각화하는 도구이다.**
 - **좌표계 확인**
     - RViz2좌측 패널의 Displays에서 Add를 클릭한다.
     - rviz_default_plugins/TF를 클릭하여 추가한다.
 - **변환 확인**
     - TF디스플레이에서 Show Arrows옵션을 체크하면 각 부모-자식 좌표계 간의 변환 방향을 화살표로 시각화하여 확인할 수 있고, 화살표의 시작점은 부모 좌표계, 끝점은 자식 좌표계이다.
     - Show Axes를 체크하면 각 좌표계의 X, Y, Z 축을 시각적으로 확인할 수 있고, 축의 방향을 통해 변환된 좌표계의 방향을 파악할 수 있다.
 - **트리 확인**
     - ros2 run rqt_tf_tree rqt_tf_tree --force-discover
     - 이 명령어는 현재 발행되고 있는 모든 TF 변환을 기반으로 트리 구조를 그려준다.
     - 각 노드는 좌표계를 나타내고, 연결선은 변환 관계를 나타낸다.

### 4-3. ROS2의 시뮬레이션 환경에서 TF(Transform Frames)이 무엇인지를 조사해보자.
 **ROS2 시뮬레이션에서 TF는 로봇의 내부 구조, 센서 데이터, 외부 환경 객체 간의 3D 공간 관계를 정확하게 표현하고 위치와 방향 정보를 실시간으로 관리하고 제공하는 프레임워크이다.**

 - **로봇 모델의 자세 표현**
     - 시뮬레이션 환경에서 로봇은 URDF(Unified Robot Description Format) 또는 XACRO 파일을 통해 정의된다. 
     - 이 파일들은 로봇의 각 링크(link)와 조인트(joint)를 정의하며, 각 링크는 고유한 좌표계를 가진다.
     - 시뮬레이션 엔진은 이 정의를 바탕으로 로봇의 물리적 모델을 생성하고, TF를 사용하여 각 링크의 현재 자세(위치와 방향)를 지속적으로 발행(publish)한다.

 - **센서 데이터 통합**
     - 시뮬레이션 내의 카메라, 라이다, IMU 등 다양한 센서들은 각각 고유한 좌표계를 가진다. 
     - 센서가 데이터를 발행할 때, 해당 데이터는 센서 자신의 좌표계에서 측정된다. 
     - TF는 이 센서 좌표계를 로봇의 base_link나 world 좌표계와 같은 다른 좌표계로 변환하여 데이터를 통합하고 로봇의 전체적인 상태를 파악하는 데 사용된다. 
     - 예를 들어, 카메라가 특정 물체를 감지했을 때, TF를 사용하여 해당 물체의 위치를 world 좌표계에서 파악할 수 있다.

 - **운동학 및 역운동학**
     - 시뮬레이션에서 로봇의 팔을 움직이거나 특정 지점으로 이동시키는 경우, TF는 순운동학(Forward Kinematics) 및 역운동학(Inverse Kinematics) 계산에 활용된다.
     - 순운동학은 조인트 각도로부터 엔드 이펙터의 자세를 계산하고, 역운동학은 엔드 이펙터의 목표 자세로부터 필요한 조인트 각도를 계산하고, 이 모든 계산은 TF 트리를 기반으로 이루어진다.

 - **환경 객체와의 상호작용**
     - 시뮬레이션 환경 내의 정적인 또는 동적인 객체들도 TF를 통해 자신의 위치와 방향을 나타낼 수 있다. 이를 통해 로봇이 환경 객체와 어떻게 상호작용하는지 (예: 충돌 감지, 특정 객체로 이동)를 시뮬레이션하고 분석할 수 있다.

### 4-4. Displays > RobotModels의 선택을 취소하고 Display > TF를 선택해보자. 이 상황에서 화면에 표시된 그림이 무엇인지 확인한다. 이를 위해서 모든 TF > Frames에서 모두 선택을 취소한 후 base_link만 선택해 확인해 본다.
이 상황에서 RViz2 화면에 표시되는 그림은 base_link 좌표계의 3D 축(Axis)이다.   
일반적으로 base_link는 로봇의 기준이 되는 좌표계이며, RViz2의 3D 뷰에서 원점(0,0,0)에 위치한다.
 - **붉은색 선(Red Line)**: X축으로 로봇의 앞쪽(Forward) 방향을 나타낸다.
 - **녹색 선(Green Line)**: Y축으로 로봇의 왼쪽(Left) 방향을 나타낸다.
 - **파란색 선(Blue Line)**: Z축으로 로봇의 위쪽(Up) 방향을 나타낸다.
이러한 색상 규칙은 ROS를 포함한 많은 3D 그래픽 및 로봇 공학 환경에서 일반적으로 사용되는 **오른손 법칙(Right-Hand Rule)**을 따른다.   
**오른손의 엄지를 X축, 검지를 Y축, 중지를 Z축 방향으로 향하게 하면 각 축의 양의 방향을 나타낼 수 있다.**  
RobotModel을 비활성화했기 때문에 로봇의 시각적인 모델은 보이지 않고, 대신 base_link라는 이름의 좌표계가 어디에 있고 어떤 방향을 향하고 있는지를 이 3D 축을 통해 시각적으로 확인할 수 있다.  

### 4-5. RViz2의 Joint State Publisher를 사용해 튜토리얼 로봇의 각 조인트의 상태를 변화시켜보자.
 - Joint State Publisher에서 각 바퀴의 조인트 상태를 변경하면서 X, Y, Z축이 어떻게 변하는지 확인할 수 있다.
 - Joint State Publisher에서 그리퍼의 조인트 상태를 변경하면서 X, Y, Z축이 어떻게 변하는지 확인할 수 있다.



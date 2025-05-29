# 수행목표
ROS2의 서비스에 대해서 알아보고, 서비스 서버와 클라이언트를 파이썬으로 구현한다.

## 1. ROS2의 서비스 서버/클라이언트에 대해서 학습한다.
 - 서비스는 ROS2에서 요청(Request)을 보내면 응답(Response)을 받는 통신을 한다.
 - 서비스는 일회성이며, 지속적으로 메시지를 주고받는 토픽과 달리 요청을 보냈을 때만 응답이 온다.
 - Client node--> (Request)--> Server node
 - Servers node--> (Response)--> Client node

## 2. 터미널에서 ROS2의 노드에서 제공하는 서비스의 목록을 확인하는 방법, 서비스를 호출하는데 필요한 정보를 확인하는 방법과 서비스를 호출하는 방법을 조사한다.
### 2-1. 서비스 목록 확인
 - ros2 service list
 - ros2 service list -t  # 서비스 목록과 데이터 타입을 한번에 확인할 수 있다.
### 2-2. 서비스 데이터 타입 확인
 - ros2 service type (/서비스 이름)
### 2-3. 서비스 타입의 요청/응답 구조 확인
 - ros2 interface show (/서비스 타입)
### 2-3. 서비스 호출
 - ros2 service call (/서비스 이름) (/서비스 타입) "{타입 구조}"

## 3. demo_nodes_cpp패키지의 add_two_ints_server 노드를 실행하고, 이 노드가 제공한 서비스를 확인한 후, 명령으로 서비스를 호출해 보고, 이 과정을 별도로 기록한 후 정리한다.
### 3-1. add_two_ints_server 노드 실행
ros2 run demo_nodes_cpp add_two_ints_server
### 3-2. 서비스 목록 확인
ros2 service list  # /add_two_ints가 출력됨.
### 3-3. 서비스 데이터 타입 확인
ros2 service type /add_two_ints  # example_interfaces/srv/AddTwoInts가 출력됨.
### 3-4. 서비스 타입의 요청/응답 구조 확인
ros2 interface show example_interfaces/srv/AddTwoInts  # 서비스 타입의 구조가 출력됨.
### 3-5. 서비스 호출
ros2 service call /add_two_ints example_interfaces/srv/AddTwoInts "{a: 7, b: 11}"

## 4. 노드를 제어하는 과정에서 노드 제어 프로그램을 처리되지 않은 예외가 발생하지 않고, 정상적으로 종료 시키는 방법을 찾는다.


## 5. ROS2 파이썬 프로그램에서 호출된 서비스를 처리하거나 다른 노드의 서비스를 호출하는 방법을 조사한다.
1. 이 과정에서 필요한 파이썬 비동기 처리 방식에 대해서 조사한다.

## 6. 이전 문제의 제어 노드 프로그램에 다음과 같이 동작하는 서비스 서버와 클라이언트를 추가로 구현한다.(turtle_move_control.py)
1. turtlesim 노드는 /kill 서비스를 제공한다. 이 서비스를 호출하는 서비스 클라이언트를 추가한다.
2. 이전 프로그램에서 만든 제어 노드 프로그램에 /quit 서비스를 추가한다. /quit 서비스가 전달되면 제어 노드 프로그램이 종료하고, turtlesim의 /kill 서비스를 클라이언트를 통해 호출해 시뮬레이터 화면에 로봇을 지우고 빈 화면을 만든다.
3. /kill 서비스를 호출한 후, 서비스 호출 결과가 반환되는 동안에도 turtle_move_control 노드는 계속 하던 일을 수행해야 한다.
4. 이 과정에서 처리되지 않은 예외가 발생하지 않아야 한다.

## 7. 구현한 프로그램을 실행한 후 터미널에서 /quit 서비스를 호출하고, 그 결과를 확인한다.

## 8. 조사한 내용을 형식 문서로 만들고 워크 스페이스 디렉토리를 압축해 함께 게시한다.
프로젝트 루트의 2/11 디렉토리를 생성한 후, 이 디렉토리 내에 문서 파일의 이름은 11_service.md(마크다운 파일의 경우)으로 저장, 게시한다. 워크스페이스 디렉토리를 압축한 파일도 함께 게시한다.
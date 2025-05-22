# 2초에 한 번씩 호출되는 타이머를 생성한다.
# 이 타이머의 콜백 함수는 로그에 "2 seconds passed"를 기록한다.

import rclpy # rclpy는 ROS2 Python 클라이언트 라이브러리로 ROS2 노드를 만들고 실행할 수 있게 해준다.
from rclpy.node import Node #  ROS2에서 노드를 정의하기 위한 기본 클래스로 모든 사용자 정의 노드는 이 클래스를 상속받아야 한다.

class TimerNode(Node):
    def __init__(self):
        super().__init__('timer_node')
        # 2초에 한 번씩 timer_callback 함수 실행
        self.timer = self.create_timer(2.0, self.timer_callback)

    def timer_callback(self):
        self.get_logger().info('2 seconds passed')

def main(args=None):
    rclpy.init(args=args)
    node = TimerNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

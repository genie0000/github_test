# 거북이 원 그리는 토픽 발행

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class CirclePublisher(Node):
    def __init__(self):
        super().__init__('circle_Publisher')
        # Twist 데이터 타입을 쓰고 있는 /turtle1/cmd_vel 토픽을 발행한다.
        self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        timer_period = 0.5  # 0.5초마다 메시지 발행 (50Hz)
        # 실행해야 될 콜백 함수는 timer_callback 이다.
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = Twist()
        msg.linear.x = 5.0    # 전진 속도
        msg.angular.z = 5.0   # 회전 속도
        self.publisher.publish(msg)
        self.get_logger().info(f'Publishing: linear.x={msg.linear.x}, angular.z={msg.angular.z}')

def main(args=None):
    rclpy.init(args=args)
    node = CirclePublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
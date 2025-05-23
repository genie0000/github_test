import rclpy
from rclpy.node import Node

class TimerNode(Node):
    def __init__(self):
        super().__init__('timer_node')

        self.counter = 0

        # 2초마다 출력 및 증가
        self.timer_2s = self.create_timer(2.0, self.timer_2s_callback)

        # 3초마다 출력 및 감소
        self.timer_3s = self.create_timer(3.0, self.timer_3s_callback)

    def timer_2s_callback(self):
        self.counter += 1
        self.get_logger().info(f'2 seconds passed : {self.counter}')

    def timer_3s_callback(self):
        self.counter -= 1
        self.get_logger().info(f'3 seconds passed : {self.counter}')

def main(args=None):
    rclpy.init(args=args)
    node = TimerNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

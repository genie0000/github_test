import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from std_srvs.srv import Empty
from turtlesim.srv import Kill

import math

class TurtleControlNode(Node):
    def __init__(self):
        super().__init__('turtle_move_control')
        self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.subscriber = self.create_subscription(Pose, '/turtle1/pose', self.pose_callback, 10)
        self.quit_service = self.create_service(Empty, '/quit', self.quit_callback)
        self.kill_client = self.create_client(Kill, '/kill')

        self.timer = self.create_timer(0.1, self.control_loop)

        self.pose = None
        self.keep_running = True
        self.kill_future = None

    def pose_callback(self, msg):
        self.pose = msg

    def control_loop(self):
        if not self.keep_running:
            return  # quit 요청 후에는 아무것도 하지 않음

        # kill 서비스 응답 기다리는 동안도 동작 계속
        if self.kill_future:
            if self.kill_future.done():
                try:
                    result = self.kill_future.result()
                    self.get_logger().info("Turtle killed successfully.")
                except Exception as e:
                    self.get_logger().error(f"Kill service failed: {e}")
                finally:
                    self.kill_future = None  # 다시 초기화

        # pose 없으면 패스
        if self.pose is None:
            return

        # 벽 근처이면 회전
        if self.pose.x < 2.0 or self.pose.x > 9.0 or self.pose.y < 2.0 or self.pose.y > 9.0:
            twist = Twist()
            twist.linear.x = 1.0
            twist.angular.z = 1.0  # 회전
        else:
            twist = Twist()
            twist.linear.x = 2.0
            twist.angular.z = 0.0  # 직진

        self.publisher.publish(twist)

    def quit_callback(self, request, response):
        self.get_logger().info('Received quit service call.')

        # kill 요청 보내기
        if self.kill_client.service_is_ready():
            req = Kill.Request()
            req.name = 'turtle1'
            self.kill_future = self.kill_client.call_async(req)
            self.get_logger().info('Sent kill request for turtle1.')
        else:
            self.get_logger().error('/kill 서비스가 준비되지 않았습니다.')

        self.keep_running = False  # 제어 멈추기 (단, kill 결과는 비동기로 계속 처리)

        return response


def main(args=None):
    rclpy.init(args=args)
    node = TurtleControlNode()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Keyboard interrupt, shutting down.')

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

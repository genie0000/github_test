import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math
import random

class TurtleMoveControl(Node):
    def __init__(self):
        super().__init__('turtle_move_control')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.subscription = self.create_subscription(Pose, '/turtle1/pose', self.pose_callback, 10)
        
        self.pose = None
        self.timer = self.create_timer(0.1, self.control_loop)  # 10Hz
        self.turning = False
        self.turn_count = 0

    def pose_callback(self, msg):
        self.pose = msg

    def control_loop(self):
        if self.pose is None:
            return
        
        msg = Twist()

        # 거북이의 현재 좌표
        x = self.pose.x
        y = self.pose.y

        # 벽에서 얼마나 떨어져 있는지 확인
        distance_to_wall = min(x - 0.5, 11.0 - x, y - 0.5, 11.0 - y)

        # 회전 조건: 벽에 너무 가까워졌을 때
        if distance_to_wall < 1.0 or self.turning:
            self.turning = True
            msg.linear.x = 1.5
            msg.angular.z = 2.0  # 곡선 회전
            self.turn_count += 1

            # 일정 시간 회전 후 다시 직진
            if self.turn_count > 15:
                self.turning = False
                self.turn_count = 0
        else:
            # 직진
            msg.linear.x = 2.0
            msg.angular.z = 0.0

        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = TurtleMoveControl()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

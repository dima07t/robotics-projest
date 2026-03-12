import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan


class SmartRobotController(Node):

    def __init__(self):
        super().__init__('smart_robot_controller')
        self.cmd_pub = self.create_publisher(Twist, '/cmd_vel', 10)

        self.scan_sub = self.create_subscription(
            LaserScan,
            '/scan',
            self.scan_callback,
            10
        )

        self.get_logger().info("Smart Robot Controller Started")

    def scan_callback(self, msg):


        front_distance = msg.ranges[len(msg.ranges)//2]

        cmd = Twist()

    
        if front_distance < 0.6:
            self.get_logger().info("Obstacle detected, turning")

            cmd.linear.x = 0.0
            cmd.angular.z = 0.5

        else:
            self.get_logger().info("Path clear, moving forward")

            cmd.linear.x = 0.2
            cmd.angular.z = 0.0

        self.cmd_pub.publish(cmd)


def main(args=None):

    rclpy.init(args=args)

    node = SmartRobotController()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if name == '__main__':
    main()

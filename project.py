import rclpy
from rclpy.node import Node
from geometry_msgs.msg import TwistStamped
from sensor_msgs.msg import LaserScan
import numpy as np

class MappingRobot(Node):
    def __init__(self):
        super().__init__('mapping_robot')

        self.publisher = self.create_publisher(TwistStamped, '/cmd_vel', 10)
        self.scan_sub = self.create_subscription(LaserScan, '/scan', self.scan_callback, 10)

        self.declare_parameter('max_speed', 0.15)
        self.max_speed = self.get_parameter('max_speed').value
        
        self.state = "FORWARD"
        self.min_front_distance = 10.0
        
        self.timer = self.create_timer(0.1, self.control_loop)
        self.get_logger().info('Mapping Robot Node started')

    def scan_callback(self, msg):
        front_sector = []
        for i in range(-30, 31):
            dist = msg.ranges[i]
            if msg.range_min < dist < msg.range_max:
                front_sector.append(dist)
        
        if front_sector:
            self.min_front_distance = min(front_sector)
        else:
            self.min_front_distance = 10.0

    def control_loop(self):
        msg = TwistStamped()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = 'base_link'

        if self.min_front_distance < 0.4:
            self.state = "TURNING"
        elif self.min_front_distance > 0.8:
            self.state = "FORWARD"

        if self.state == "FORWARD":
            target_speed = self.max_speed if self.min_front_distance > 1.0 else 0.05
            msg.twist.linear.x = target_speed
            msg.twist.angular.z = 0.0
        
        elif self.state == "TURNING":
            msg.twist.linear.x = 0.0
            msg.twist.angular.z = 0.5

        self.publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = MappingRobot()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        stop_msg = TwistStamped()
        node.publisher.publish(stop_msg)
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()

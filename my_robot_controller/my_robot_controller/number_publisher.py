#!/bin/python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class Talker(Node):

    def __init__(self):
        super().__init__('number_publisher')
        self.publisher_ = self.create_publisher(Int32, 'number_topic', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        # self.msg_ = String()

    def timer_callback(self):
        msg = Int32()
        msg.data = 1  # Example integer value
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%d"' % msg.data)
        
def main(args=None):
    rclpy.init(args=args)
    talker = Talker()
    rclpy.spin(talker)
    # talker.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

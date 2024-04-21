#!/bin/python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class Listener(Node):

    def __init__(self):
        super().__init__('number_subscriber')
        self.subscription = self.create_subscription(
            Int32,
            'number_topic',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%d"' % msg.data)

def main(args=None):
    rclpy.init(args=args)
    listener = Listener()
    rclpy.spin(listener)
    # listener.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

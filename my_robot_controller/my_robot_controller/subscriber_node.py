#!/bin/python3
import rclpy
from rclpy.node import Node

class Subscriber(Node):

    def __init__(self):
        super().__init__("subscriber_node")
        self.get_logger().info("helloooo")

def main(args=None):
    rclpy.init(args=args)
    subscriber_node = Subscriber()
    rclpy.spin(subscriber_node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
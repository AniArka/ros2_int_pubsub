#!/bin/python3
import rclpy
from rclpy.node import Node

class Publisher(Node):

    def __init__(self):
        super().__init__("publisher_node")
        self.get_logger().info("hello")

# class Subscriber(Node):

#     def __init__(self):
#         super().__init__("subscriber_node")
#         self.get_logger().info("helloooo")

def main(args=None):
    rclpy.init(args=args)
    publisher_node = Publisher()
    # subscriber_node = Subscriber()
    rclpy.spin(publisher_node)
    # rclpy.spin(subscriber_node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
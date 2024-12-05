import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Robot1(Node):
    def __init__(self):
        super().__init__('robot1')
        self.subscription = self.create_subscription(
            String,
            'bascorro',
            self.subscriber_msg,
            10
        )

    def subscriber_msg(self, msg):
        self.get_logger().info(f'Received: "{msg.data}"')

def main(args=None):
    rclpy.init(args=args)
    node = Robot1()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

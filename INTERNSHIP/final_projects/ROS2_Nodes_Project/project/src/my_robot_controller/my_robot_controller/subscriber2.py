import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from example_interfaces.srv import AddTwoInts

class Robot2(Node):
    def __init__(self):
        super().__init__('robot2')
        self.subscription = self.create_subscription(
            String,
            'bascorro',
            self.subscribe_msg,
            10
        )

    
        """
        SERVICE CLIENT
        """
        self.client = self.create_client(AddTwoInts, 'jumlah')
        self.timer_client = self.create_timer(2.0, self.call_service)

        self.get_logger().info('Combined Node initialized')

    def subscribe_msg(self, msg):
        self.get_logger().info(f'Received: "{msg.data}"')

    def call_service(self):
        if not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().warn('Gak ad Service')
            return

        request = AddTwoInts.Request()
        request.a = 6
        request.b = 9

        future = self.client.call_async(request)
        future.add_done_callback(self.service_response_callback)

    def service_response_callback(self, future):
        try:
            response = future.result()
            self.get_logger().info(f'Service Response: {response.sum}')
        except Exception as e:
            self.get_logger().error(f'Error {e}')

def main(args=None):
    rclpy.init(args=args)
    node = Robot2()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

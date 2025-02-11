import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from example_interfaces.srv import AddTwoInts


class Gue(Node):
    def __init__(self):
        super().__init__("Gue")
        self.publisher_ = self.create_publisher(String, "bascorro", 10)
        self.counter_ = 0
        self.create_timer(1.0, self.timer_callback)

        # Service Server
        self.service = self.create_service(
            AddTwoInts, "add_two_ints", self.handle_service
        )

    def handle_service(self, request, response):
        response.sum = request.a + request.b
        self.get_logger().info(
            f"Service called: {request.a} + {request.b} = {response.sum}"
        )
        return response

    def timer_callback(self):
        msg = String()
        msg.data = f"HALO {self.counter_}"
        self.publisher_.publish(msg)
        self.get_logger().info("Publishing...")
        self.counter_ += 1


def main(args=None):
    rclpy.init(args=args)
    node = Gue()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()

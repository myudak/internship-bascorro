import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from example_interfaces.srv import AddTwoInts

class Gue(Node):
    def __init__(self):
        super().__init__('Gue')
        self.counter_ = 0
        
        """
        PUBLISHER
        """
        self.publisher_ = self.create_publisher(String, 'bascorro', 10)
        self.create_timer(1.0,self.publis_msg)

        """
        SERVICE SERVER
        """
        self.service = self.create_service(
            AddTwoInts,
            'jumlah',
            self.service_jumlah
        )

    def publis_msg(self):
        msg = String()
        msg.data = f'HALO {self.counter_}'
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing...')
        self.counter_ += 1

    def service_jumlah(self, request, response):
        response.sum = request.a + request.b
        self.get_logger().info(f'Service called: {request.a} + {request.b} = {response.sum}')
        return response

    

def main(args=None):
    rclpy.init(args=args)
    node = Gue()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

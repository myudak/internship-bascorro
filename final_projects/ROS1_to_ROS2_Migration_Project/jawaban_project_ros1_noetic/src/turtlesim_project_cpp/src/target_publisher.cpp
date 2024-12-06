#include <rclcpp/rclcpp.hpp>
#include <my_robot_msgs/msg/coordinates2_d.hpp>
#include <random>

class TargetPublisher : public rclcpp::Node
{
public:
    TargetPublisher() : Node("target_publisher")
    {
        this->declare_parameter<double>("publish_interval", 3.0);
        double publish_interval = this->get_parameter("publish_interval").as_double();

        pub_ = this->create_publisher<my_robot_msgs::msg::Coordinates2D>("target_coordinates", 10);
        timer_ = this->create_wall_timer(std::chrono::duration<double>(publish_interval), std::bind(&TargetPublisher::sendRandomCoordinates, this));
        RCLCPP_INFO(this->get_logger(), "Target publisher has been started");
    }

private:
    rclcpp::Publisher<my_robot_msgs::msg::Coordinates2D>::SharedPtr pub_;
    rclcpp::TimerBase::SharedPtr timer_;
    std::mt19937 rng_{std::random_device{}()};
    std::uniform_real_distribution<double> dist_{0.0, 11.0};

    double randomDouble()
    {
        return dist_(rng_);
    }

    void sendRandomCoordinates()
    {
        double x = randomDouble();
        double y = randomDouble();
        publishCoordinates(x, y);
    }

    void publishCoordinates(double x, double y)
    {
        auto msg = my_robot_msgs::msg::Coordinates2D();
        msg.x = x;
        msg.y = y;
        pub_->publish(msg);
    }
};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<TargetPublisher>());
    rclcpp::shutdown();
    return 0;
}
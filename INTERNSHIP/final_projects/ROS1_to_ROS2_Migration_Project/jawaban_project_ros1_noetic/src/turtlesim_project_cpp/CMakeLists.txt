cmake_minimum_required(VERSION 3.5)
project(turtlesim_project_cpp)

# Compile as C++11, supported in ROS2
add_compile_options(-std=c++17)

find_package(ament_cmake REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(rclcpp REQUIRED)
find_package(turtlesim REQUIRED)
find_package(my_robot_msgs REQUIRED)

ament_export_dependencies(geometry_msgs rclcpp turtlesim my_robot_msgs)

include_directories(
  ${ament_INCLUDE_DIRS}
)

add_executable(target_publisher src/target_publisher.cpp)
ament_target_dependencies(target_publisher rclcpp geometry_msgs turtlesim my_robot_msgs)

add_executable(turtle_controller src/turtle_controller.cpp)
ament_target_dependencies(turtle_controller rclcpp geometry_msgs turtlesim my_robot_msgs)

ament_package()

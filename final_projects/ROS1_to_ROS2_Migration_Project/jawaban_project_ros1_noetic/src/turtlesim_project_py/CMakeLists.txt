cmake_minimum_required(VERSION 3.5)
project(turtlesim_project_py)

find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(turtlesim REQUIRED)
find_package(geometry_msgs REQUIRED)

ament_export_dependencies(rclpy turtlesim geometry_msgs)

include_directories(
  ${ament_INCLUDE_DIRS}
)

ament_package()

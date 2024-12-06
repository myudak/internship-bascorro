from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    # Create launch configuration variables
    publish_interval = LaunchConfiguration('publish_interval', default='2.0')

    # Declare launch arguments
    declare_publish_interval_arg = DeclareLaunchArgument(
        'publish_interval',
        default_value='2.0',
        description='Publishing interval for target generator'
    )

    # Create node descriptions
    turtlesim_node = Node(
        package='turtlesim',
        executable='turtlesim_node',
        name='turtlesim',
        output='screen'
    )

    turtle_controller_node = Node(
        package='turtlesim_project_py',
        executable='turtle_controller',
        name='turtle_controller',
        output='screen'
    )

    target_generator_node = Node(
        package='turtlesim_project_cpp',
        executable='target_publisher',
        name='target_generator',
        output='screen',
        parameters=[{
            'publish_interval': publish_interval
        }]
    )

    # Return launch description
    return LaunchDescription([
        declare_publish_interval_arg,
        turtlesim_node,
        turtle_controller_node,
        target_generator_node
    ])

#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist, Point, Quaternion
from sensor_msgs.msg import LaserScan
from nav_msgs.msg import Odometry
import tf
from tf.transformations import euler_from_quaternion, quaternion_from_euler
import time
from math import radians, copysign, sqrt, pow, pi
import PyKDL


class RobotControl:

    def __init__(self):
        rospy.init_node("robot_control_node", anonymous=True)
        self.vel_publisher = rospy.Publisher("/cmd_vel", Twist, queue_size=1)
        self.summit_vel_publisher = rospy.Publisher(
            "/summit_xl_control/cmd_vel", Twist, queue_size=1
        )
        self.laser_subscriber = rospy.Subscriber(
            "/kobuki/laser/scan", LaserScan, self.laser_callback
        )
        self.summit_laser_subscriber = rospy.Subscriber(
            "/hokuyo_base/scan", LaserScan, self.summit_laser_callback
        )
        self.odom_sub = rospy.Subscriber("/odom", Odometry, self.odom_callback)
        self.cmd = Twist()
        self.laser_msg = LaserScan()
        self.summit_laser_msg = LaserScan()
        self.roll = 0.0
        self.pitch = 0.0
        self.yaw = 0.0
        self.ctrl_c = False
        self.rate = rospy.Rate(10)
        self.tf_listener = tf.TransformListener()
        self.odom_frame = "/odom"
        self.base_frame = "/base_link"
        self.angular_tolerance = radians(2)
        rospy.on_shutdown(self.shutdownhook)

    def publish_once_in_cmd_vel(self):
        while not self.ctrl_c:
            connections = self.vel_publisher.get_num_connections()
            summit_connections = self.summit_vel_publisher.get_num_connections()
            if connections > 0 or summit_connections > 0:
                self.vel_publisher.publish(self.cmd)
                self.summit_vel_publisher.publish(self.cmd)
                break
            else:
                self.rate.sleep()

    def shutdownhook(self):
        self.ctrl_c = True

    def laser_callback(self, msg):
        self.laser_msg = msg

    def summit_laser_callback(self, msg):
        self.summit_laser_msg = msg

    def odom_callback(self, msg):
        orientation_q = msg.pose.pose.orientation
        orientation_list = [
            orientation_q.x,
            orientation_q.y,
            orientation_q.z,
            orientation_q.w,
        ]
        (self.roll, self.pitch, self.yaw) = euler_from_quaternion(orientation_list)

    def get_laser(self, pos):
        time.sleep(1)
        return self.laser_msg.ranges[pos]

    def get_laser_summit(self, pos):
        time.sleep(1)
        return self.summit_laser_msg.ranges[pos]

    def get_front_laser(self):
        time.sleep(1)
        return self.laser_msg.ranges[360]

    def get_laser_full(self):
        time.sleep(1)
        return self.laser_msg.ranges

    def stop_robot(self):
        self.cmd.linear.x = 0.0
        self.cmd.angular.z = 0.0
        self.publish_once_in_cmd_vel()

    def move_straight(self):
        self.cmd.linear.x = 0.5
        self.cmd.linear.y = 0
        self.cmd.linear.z = 0
        self.cmd.angular.x = 0
        self.cmd.angular.y = 0
        self.cmd.angular.z = 0
        self.publish_once_in_cmd_vel()

    def move_straight_time(self, motion, speed, time):
        self.cmd.linear.y = 0
        self.cmd.linear.z = 0
        self.cmd.angular.x = 0
        self.cmd.angular.y = 0
        self.cmd.angular.z = 0
        self.cmd.linear.x = speed if motion == "forward" else -speed

        for _ in range(int(time * 10)):
            self.vel_publisher.publish(self.cmd)
            self.summit_vel_publisher.publish(self.cmd)
            self.rate.sleep()
        self.stop_robot()

    def turn(self, clockwise, speed, time):
        self.cmd.linear.x = 0
        self.cmd.linear.y = 0
        self.cmd.linear.z = 0
        self.cmd.angular.x = 0
        self.cmd.angular.y = 0
        self.cmd.angular.z = -speed if clockwise == "clockwise" else speed

        for _ in range(int(time * 10)):
            self.vel_publisher.publish(self.cmd)
            self.summit_vel_publisher.publish(self.cmd)
            self.rate.sleep()
        self.stop_robot()

    # Additional methods from the second script...


MENU_1 = """
==========|@myudak|============
1 / belok : robot belok,
2 / lurus : robot lurus,
e / exit : exit,
==========|@myudak|============
> """
MENU_2 = """
==========|belok|============
1 / cc : counter clockwise kebalikan jarum jam,
2 / c : clockwise jarum jam,
==========|@myudak|============
> """
MENU_3 = """
==========|lurus|============
1 / maju : robot maju,
2 / mundur : robot mundur,
==========|@myudak|============
> """


def menu2_pilih(prompt):
    return "clockwise" if prompt in ("2", "c") else "counter-clockwise"


def menu3_pilih(prompt):
    return "forward" if prompt in ("1", "maju") else "backward"


def input_angka(prompt):
    try:
        return float(input(prompt))
    except ValueError:
        print("number dongo")
        return input_angka(prompt)


def main():
    RC = RobotControl()
    commands = []

    while True:
        inputny = input(MENU_1).strip().lower()
        if inputny in ("exit", "e"):
            break
        elif inputny in ("1", "belok"):
            direction = menu2_pilih(input(MENU_2).strip().lower())
            speed = input_angka("Enter speed: ")
            duration = input_angka("Enter duration: ")
            RC.turn(direction, speed, duration)
            commands.append(f'RC.turn("{direction}", {speed}, {duration})')
        elif inputny in ("2", "lurus"):
            direction = menu3_pilih(input(MENU_3).strip().lower())
            speed = input_angka("Speed > ")
            duration = input_angka("Durasi > ")
            RC.move_straight_time(direction, speed, duration)
            commands.append(
                f'RC.move_straight_time("{direction}", {speed}, {duration})'
            )
        else:
            print("dongo ajg")

    print("\nCommand")
    for command in commands:
        print(command)


if __name__ == "__main__":
    main()

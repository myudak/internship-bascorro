from robot_control_class import RobotControl

rc = RobotControl()

a = rc.get_laser_full()

print(a[0])
print(a[360])
print(a[719])

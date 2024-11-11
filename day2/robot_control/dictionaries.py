from robot_control_class import RobotControl

rc = RobotControl()

a = rc.get_laser_full()

print(
    {
        "P0": a[0],
        "P100": a[100],
        "P200": a[200],
        "P300": a[300],
        "P400": a[400],
        "P500": a[500],
        "P600": a[600],
        "P719": a[719],
    }
)

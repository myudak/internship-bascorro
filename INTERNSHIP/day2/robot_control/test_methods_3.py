from robot_control_class import RobotControl

RC = RobotControl()
commands = []

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
    if prompt == "2" or prompt == "c":
        return "clockwise"
    if prompt == "1" or prompt == "cc":
        return "counter-clockwise"


def menu3_pilih(prompt):
    if prompt == "1" or prompt == "lurus":
        return "forward"
    if prompt == "2" or prompt == "mundur":
        return "backward"


def input_angka(prompt):
    try:
        return float(input(prompt))
    except ValueError:
        print("number dongo")
        return input_angka(prompt)


def main():
    while 1:
        inputny = input(MENU_1).strip().lower()

        if inputny == "exit" or inputny == "e":
            break

        if inputny == "1" or inputny == "belok":
            direction = menu2_pilih(input(MENU_2).strip().lower())
            speed = input_angka("Enter speed: ")
            duration = input_angka("Enter duration: ")
            RC.turn(direction, speed, duration)
            commands.append(f'robotcontrol.turn("{direction}", {speed}, {duration})')
            continue
        if inputny == "2" or inputny == "lurus":
            direction = menu3_pilih(input(MENU_3).strip().lower())
            speed = input_angka("Speed >")
            duration = input_angka("Durasi >")
            RC.move_straight_time(direction, speed, duration)
            commands.append(
                f'robotcontrol.move_straight_time("{direction}", {speed}, {duration})'
            )
            continue
        print("dongo ajg")

    print("\nCommand")
    for command in commands:
        print(command)


if __name__ == "__main__":
    main()

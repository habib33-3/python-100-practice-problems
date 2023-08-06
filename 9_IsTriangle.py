# 9. Write a program that take a user input of three angles and will find out whether it can form a triangle or not.


def is_triangle(angle1, angle2, angle3):
    if (angle1+angle2+angle3 == 180):
        print("It is a triangle")
    else:
        print("its not a triangle")


angle1, angle2, angle3 = map(float, input().split())

is_triangle(angle1, angle2, angle3)

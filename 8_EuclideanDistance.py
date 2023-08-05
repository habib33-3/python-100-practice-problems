# 8. Write a program to find the euclidean distance between two coordinates.
import math


def calculate_euclidean_distance(x1, x2, y1, y2):
    x = (x1-x2)**2
    y = (y1-y2)**2

    distance = math.sqrt(x+y)

    print(distance)


x1, x2 = map(float, input().split())
y1, y2 = map(float, input().split())
calculate_euclidean_distance(x1, x2, y1, y2)

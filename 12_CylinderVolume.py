""""12. Write a program to find the volume of the cylinder. Also find the
cost when ,when the cost of 1litre milk is 40Rs"""


def calculate_volume(height, radius):
    PI = 3.1416

    volume = PI*(radius**2)*height

    return volume


height, radius = map(float, input().split())
volume = calculate_volume(height, radius)
MilkPrice = volume*40

print(f"volume is {volume} litre and the price of milk is {MilkPrice} taka ")

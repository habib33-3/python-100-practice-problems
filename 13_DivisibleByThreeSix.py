"""
Write a program that will tell whether the given number is divisible
by 3 & 6.
    """


def divisible(n):
    if n % 3 == 0 and n % 6 == 0:
        print("Divisible")
    else:
        print("Not divisible")


n = int(input())

divisible(n)

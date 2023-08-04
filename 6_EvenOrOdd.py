# 6. Write a program that will tell whether the number entered by the user is odd or even.



def even_odd(number):
    if number % 2 == 0:
        print("even")
    print("odd")


num = int(input())
even_odd(num)

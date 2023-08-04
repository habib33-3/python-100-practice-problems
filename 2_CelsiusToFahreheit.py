# 2. Write a program that will convert celsius value to fahrenheit

def celsius_to_fahrenheit(temperature):
    fahrenheit = (temperature*(9/5)+32)

    print(fahrenheit)


celsius = int(input())

celsius_to_fahrenheit(celsius)

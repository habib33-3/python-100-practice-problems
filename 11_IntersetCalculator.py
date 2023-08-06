# 11. Write a program to find the simple interest when the value of principle,rate of interest and time period is given.

def interest_calculator(principle, interest_rate, year):
    interest = (principle*interest_rate*year)/100

    print(
        f"Total interest of {principle} at the interest rate of {interest_rate} in time period of {year} year is : {interest}")


principle = float(input("Enter principle: "))
interest_rate = float(input("Enter interest rate: "))
year = float(input("Enter  year: "))

interest_calculator(principle, interest_rate, year)

# 10. Write a program that will take user input of cost price and selling price and determines whether its a loss or a profit

def profit_or_loss(cost, selling_price):
    if (selling_price > cost):
        print("It is profit")
    else:
        print("It is loss")


cost = int(input())
selling_price = int(input())

profit_or_loss(cost, selling_price)

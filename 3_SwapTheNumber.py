#  3. User will input (2numbers).Write a program to swap the numbers

def swap(first_num, second_num):

    print(f"First Number: {first_num}")
    print(f"Second Number: {second_num}")

    first_num, second_num = second_num, first_num

    print("After Swap")

    print(f"First Number: {first_num}")
    print(f"Second Number: {second_num}")


FirstNum = int(input())
SecondNum = int(input())
swap(FirstNum, SecondNum)

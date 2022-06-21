# Write code for algorithm 1 below
# 1. Write a program that takes a positive number as an argument and prints the numbers from n to zero.

def countdown(number):
    if number == 0:
        return
    print(number)
    countdown(number-1)

countdown(10)
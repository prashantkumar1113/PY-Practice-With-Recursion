# Write code for algorithm 2 below
# 2. Write a function that prints the natural numbers from 1 to n.

def natural_numbers(x,i = 1):
    if x == 0:
        return
    print(i)
    natural_numbers(x-1, i+1)
natural_numbers(10)
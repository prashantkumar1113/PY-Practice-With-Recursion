# Write code for algorithm 3 below
# Write a function that returns the nth elements in the Fibonacci Sequence.
# The Fibonacci Sequence is the series of numbers where the next number is found by adding up the two numbers before it: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
# For example, if n=4, then the result would be '2' and if n=2, the result would be '1'
# Here is more information on the Fibonacci Sequence.
# Hint: Look back at the factorial example as the structure of the algorithm may help you.

def fibonacci(number):
    if number <= 1:
        return number
    return (fibonacci(number-1) + fibonacci(number-2))

print(fibonacci(13))
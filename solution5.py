# Write code for algorithm 5 below
# Write a function that checks whether a string is a palindrome or not. 
# The program should take in a string and return True if the string is a palindrome and False if not.
# A palindrome is a word that is the same when it is reversed, such as madam, radar, kayak, or tacocat.
# Here is more information on palindromes.

def palindrome(string):
    # print(f"first element: {string[0]}, last element: {string[-1]}")
    # print(f"len = {len(string)}")
    if len (string) < 1:
        # print("here")
        return True
    if string[0] != string[-1]:
        return False
    # print(string[1:-1])
    return palindrome(string[1:-1])

print(palindrome("hannah"))
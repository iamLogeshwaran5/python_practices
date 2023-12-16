"""
Given a string S, print 'yes' if it has a vowel in it else print 'no'.
Sample Testcase :
INPUT
codekata
OUTPUT
yes
"""
def has_vowel(string):
    vowels = 'aeiouAEIOU'  # Define a string of vowels

    for char in string:
        if char in vowels:
            return 'yes'
    
    return 'no'

# Sample Input
input_string = input("Enter a string: ")
result = has_vowel(input_string)

print(result)

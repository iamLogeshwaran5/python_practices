"""
6.Given a string 'S' print the sum of weight of the String. A weight of character is defined as the ASCII value of corresponding character.

Input Description:
You are given a string ‘s’

Output Description:
Print weight

Sample Input :
abc
Sample Output :
294

"""

def calculate_weight(string):
    weight = 0
    
    for char in string:
        weight += ord(char)  # Adding ASCII value of each character
    
    return weight

# Sample Input
input_string = input("Enter a string: ")
result = calculate_weight(input_string)

print("Weight:", result)

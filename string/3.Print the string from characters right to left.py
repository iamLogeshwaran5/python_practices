"""
 Jennyfer is fond of strings. She wants to read the character from right to left (reverse the string), so she wants you to design a suitable algorithm which satisfy her desire.

Input Description:
Enter the string ‘s’

Output Description:
Print the string from characters right to left.

Sample Input :
jennyfer
Sample Output :
Refynnej
"""
# Input the string
s = input()

# Reverse the string and capitalize the first letter
reversed_string = s[::-1].capitalize()

# Print the reversed string
print( reversed_string)


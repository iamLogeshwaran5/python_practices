"""

7.You are given a number with duplicate digits your task is to remove the immediate duplicate digits and print the result

Input Description:
You are given a long string of digits

Output Description:
Print the desired result print -1 if result length is 0

Sample Input :
1331
Sample Output :
11

"""


def remove_immediate_duplicates(s):
    stack = []
    for digit in s:
        # Check if the stack is empty or the current digit is different from the top of the stack
        if not stack or digit != stack[-1]:
            stack.append(digit)
        else:
            stack.pop()  # Remove the immediate duplicate digit

    result = ''.join(stack)
    if len(result) == 0:
        print(-1)
    else:
        print(result)

# Example input
input_str = input()
remove_immediate_duplicates(input_str)

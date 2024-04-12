"""
Given 2 numbers N and K followed by elements of N .Print 'yes' if K exists else print 'no'.
Sample Testcase :
INPUT
4 2
1 2 3 3
OUTPUT
yes
"""

# Get the input values N and K
N, K = map(int, input().split())

# Get the list of N elements
elements = list(map(int, input().split()))

# Check if K exists in the elements
if K in elements:
    print('yes')
else:
    print('no')

"""
Joyal was given a sentence. His task is to delete the two words that comes together and print the sentence so that the words in the output sentence have distinct words compared to their adjacent words. If no words are present in the output sentence print -1

Input Description:
You are given input string 'S'

Output Description:
Print the all the words that are left in the string 's' so that the words in the output sentence have distinct words compared to their adjacent words. Print -1 if no words are left

Sample Input :
I am john cena cena john
Sample Output :
I am
"""
a = list(map(str, input().split()))  # Get input and split it into a list
print(a)

b = []
for j in range(2):
    for i in range(0, len(a) - 2):
        if a[i] == a[i + 1]:
            a.pop(i)
            a.pop(i + 1)
        else:
            b.append(a[i])

print(*b)

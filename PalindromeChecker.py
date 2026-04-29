word = input("Enter the word: ")
length = len(word)#apple = 5 [0, 1, 2, 3, 4]
'''
reverse = ""
for i in range(length -1, -1, -1):
    reverse += word[i]
    print(reverse)
'''

reverse = word[::-1]

if(reverse == word):
    print("Palindrome")
else:
    print("Not Palindrome")
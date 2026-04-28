"""
Star patterns 

for i in range(rang):
    for j in range(i):
        print("*", end = " ")
    print("*")

for i in range(rang):
    print("*" * i)
*
* *
* * *
* * * *
* * * * *


for i in range(rang, 0, -1):
    print("*" * i)
*****
****
***
**
*

for i in range(rang):
    print(" " * (rang - i), end = " ")
    print("*" * i)

     *
    **
   ***
  ****


for i in range(rang):
    print(" " * i, end = " ")
    print("*" * (rang - i))

 *****
  ****
   ***
    **
     *

for i in range(rang):
    print(" " * (rang - i) ,end = "*" * (i*3 - 2))
    print("")

    *
   ****
  *******
 **********

 for i in range(rang):
    print(" " * i, end = "*" * (rang - i * 2))
    print(" ")

*****
 ***
  *



  for i in range(rang):
    for j in range(i):
        print(" " * (rang - j), end = "*" * (j * 3 -2))
        print()
    for k in range(i):
        print(" " * k, end = "*" * (rang - k));
        print();

for i in range(rang*2):
    for j in range(rang):
        print(" " * (rang - j), end = "*" * (j * 3 -2))
        print()
    for k in range(rang):
        print(" " * k, end = "*" * ((rang - k) * 2));
        print();


        for i in range(rang*2):
    for j in range(rang):
        print(" " * (rang - j), end = "*" * (j * 3 -2))
        print()


for i in range(rang):
    print(" " * (rang - i), end = "*" * (i))
    print("");


word = input("Enter a word").lower()
vo = word.count("a") + word.count("e") + word.count("i") + word.count("o") + word.count("u")
print("Vowel count is", vo)


lis  = [1, 8, 6, 7, 9]
lis.sort(reverse = True)
print("Greatest is ", lis[0])

"""

"""

for i in range(rang):
    print(" " * (rang - i), end = "*" * i)
    print("")

for i in range(rang):
    print(" " * i, end = "*" * (rang - i))
    print(" ")
"""
#rang = int(input("Enter number"))

'''for i in range(1, rang):  
    for j in range(rang - i):
        print(" ", end=" ")  
    for k in range(2 * i - 1):
        print("*", end=" ")
    print();

for i in range(rang, 0, -1):  
    for j in range(rang - i):
        print(" ", end=" ")  
    for k in range(2 * i - 1):
        print("*", end=" ")  
    print();'''

'''for i in range(rang):
    print("* " * i)'''

'''for i in range(rang, 0, -1):
    print("*" * i)'''

'''
for i in range(rang):
    print(" " * (rang - i), end = " ")
    print("*" * i)'''

'''for i in range(rang):
    print(" " * i, end = " ")
    print("*" * (rang - i))'''

'''for i in range(rang):
    print(" " * (rang - i) ,end = "*" * (i*3 - 2))
    print("")'''

'''for i in range(rang):
    print(" " * i, end = "*" * (rang - i * 2))
    print(" ")'''


'''word = input("Enter a word: ").lower()
vo = word.count("a") + word.count("e") + word.count("i") + word.count("o") + word.count("u")
print("Vowel count is", vo)
'''


lis  = [1, 8, 6, 7, 9]
lis.sort(reverse = True)
print("Greatest is ", lis[0]);
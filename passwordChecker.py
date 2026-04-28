password = input("\nEnter your password: ")
special = "~!@#$%^&*()_+"

hasDigit = False
hasUpper = False
hasLower = False
hasSpecial = False

for i in password:
    if i.isdigit():
        hasDigit = True
    if i.isupper():
        hasUpper = True
    if i.islower():
        hasLower = True
    if i in special:
        hasSpecial = True

if (len(password) >= 8 and hasDigit and hasUpper and hasLower and hasSpecial):
    print("Password is strong")
else:
    if(len(password) < 8):
        print("\n* Your password length is less than 8")
    if not hasDigit:
        print("\n* Your password does not have digit")
    if not hasUpper:
        print("\n* Your password does not have uppercase")
    if not hasLower:
        print("\n* Your password does not have lowercase")
    if not hasSpecial:
        print("\n* Your password does not have special character\n")

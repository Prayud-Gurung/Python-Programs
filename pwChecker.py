import re

pw = input("Enter the password: \n");
err = ""

def passChecker(password, strength = 0):
    global err
    if len(password) >= 8:
        strength += 1
    else:
        err += "Password is less than 8 \n"

    if re.search("[a-z]", password):
        strength += 1
    else:
        err += "missing lowercase \n"

    if re.search("[A-Z]", password):
        strength += 1
    else:
        err += "missing uppercase \n"

    if re.search("[\d]", password):
        strength += 1
    else:
        err += "missing digit \n"

    if re.search("[!@#$%^&*()_+]", password):
        strength += 1
    else:
        err += "missing special character !@#$%^&*()_+ \n"

    if not re.search(r'(.)\1', password):
        strength += 1
    else:
        err += "Has repeated letters \n"
    return strength
        

strength = passChecker(pw)
if(strength >= 7):
    print("Strong Password")
elif strength >= 5:
    print("Good Password")
    print(err)
else:
    print("Password is weak")
    print(err)
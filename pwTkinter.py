import tkinter as tk
import re

root = tk.Tk(className="PasswordChecker")
root.geometry("500x200")

label = tk.Label(root, text="Password")
entry = tk.Entry(root, background="#505050")
feedback = tk.Label(root)
label.pack()

def passChecker(password):
    strength = 0
    err = ""
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

    return strength, err

def click():
    pw = entry.get()
    strength, err = passChecker(pw)
    if strength == 6:
        feedback.configure(text="Strong Password")
    elif strength >= 4:
        feedback.configure(text="Good Password\n" + err)
    else:
        feedback.configure(text="Weak Password\n" + err)
    feedback.pack()

entry.pack()
button = tk.Button(text="go", command=click)
button.pack()

entry.config(state="normal")

root.mainloop()
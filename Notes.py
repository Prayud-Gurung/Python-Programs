File = "./Notes.txt"

def add_note(note):
    a = open(File, "a")
    a.write(note + "\n")
    a.close()

def read_note():
    try:
        a = open(File)
        output = a.read()
        print(output)
        a.close()
    except FileNotFoundError:
        print("\nNo file exists\n")

while True:
    read_note()
    text = input("Enter text: ")
    add_note(text)
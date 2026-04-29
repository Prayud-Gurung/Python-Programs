n = int(input("Enter number: "))
def fibonacci(n):
    print("\n Your output is: \n")
    a,b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

fibonacci(n)
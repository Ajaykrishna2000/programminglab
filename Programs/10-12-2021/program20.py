def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
        i = i +1
    print("The Factorial of", n, "is:",fact)
n = int(input("Enter the number:"))
factorial(n);

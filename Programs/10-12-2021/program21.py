x = 0
y = 1
n = int(input("Enter the limit:"))
print("The Fibonacci series of", n, "terms are:")
print(x)
print(y)
for i in range(2, n):
    z = x + y
    x = y
    y = z
    print(z)
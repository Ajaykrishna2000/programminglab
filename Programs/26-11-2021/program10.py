a = int(input("Enter First Number:"))
b = int(input("Enter Second Number:"))
c = int(input("Enter Third Number:"))
print("Using if-else if:")
if a > b and a > c:
    print(a, "is greatest")
elif b > a and b > c:
    print(b, "is greatest")
elif c > a and c > b:
    print(c, "is greatest")
print("Using Max:")
print(max(a, b, c), "is greatest")
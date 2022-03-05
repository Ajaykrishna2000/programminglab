a = int(input("Enter Current Year:"))
b = int(input("Enter Last Year:"))
print("The leap years form year", a, "to", b, "are:")
for num in (range(a, b)):
    if (num % 4) == 0 or (num % 400) == 0 and (num % 100) != 0:
        print(num,end="\t")
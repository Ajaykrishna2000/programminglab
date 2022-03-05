list1 = []
n = int(input("Enter the limit:"))
print("Enter the numbers:")
for i in range(0, n):
    ele = int(input())
    list1.append(ele)
print("The list of integers are:", list1)
result = [ i for i in list1 if i % 2 != 0]
print("The list after removing even numbers are:", result)
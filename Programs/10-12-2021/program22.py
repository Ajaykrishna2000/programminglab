list1 = []
sum = 0
n = int(input("Enter the limit:"))
print("Enter the numbers:")
for i in range(0, n):
    ele = int(input())
    list1.append(ele)
print("The list of numbers are:", list1)
for i in list1:
    sum = sum + i
print("The sum of items in the list:", sum)
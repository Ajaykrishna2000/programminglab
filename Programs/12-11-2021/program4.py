list1 = []
n = int(input("Enter the limit:"))
print("Enter the numbers:")
for i in range(0, n):
    ele = int(input())
    list1.append(ele)
print(list1)
result = []
for i in list1:
    if i > 100:
        result.append("Over")
    else:
        result.append(i)
print(result)
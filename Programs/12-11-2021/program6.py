list1 = []
list2 = []
list3 = []
sum1 = 0
sum2 = 0
n = int(input("Enter the limit of list1:"))
print("Enter the list of integers into list1:")
for i in range(0, n):
    ele1 = int(input())
    list1.append(ele1)
m = int(input("Enter the limit of list2:"))
print("Enter the list of integers into list2:")
for i in range(0, m):
    ele2 = int(input())
    list2.append(ele2)
print("First list is:",list1)
print("Second list is:",list2)
if len(list1) == len(list2):
    print("\na) list are of same length")
elif len(list1) < len(list2):
    print("\na) list2 is greater")
elif len(list1) > len(list2) :
    print("\na) list1 is greater")
for i in list1:
    sum1 = sum1 + i
print("\nSum of values in first list:", sum1)
for j in list2:
    sum2 = sum2 + j
print("Sum of values in second list:", sum2)
if sum1 == sum2:
    print("\nb) Sum of values on both list are same")
elif sum1 < sum2:
    print("\nb) Sum of list2 is greater")
elif sum1 > sum2:
    print("\nb) Sum of list1 is greater")
for i in list1:
    for j in list2:
        if i == j:
            list3.append(i)
print("c) The values occur in both list are:", list3)
string1 = input("Enter first string:")
string2 = input("Enter second string:")
n = len(string1)
m = len(string2)
a = string2[0]+string1[1:n]
b = string1[0]+string2[1:m]
c = a + " " + b
print("The string after combining is:", string1 + " " + string2)
print("The string after combining and swapping is:", c)
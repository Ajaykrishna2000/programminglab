a = open("learn1.txt", "r")
b = open("copy1.txt", "w")
c = a.readlines()
d = len(c)
for i in range(0,d):
    if(i%2 != 0):
        b.write(c[i])
    else:
        pass
b.close()
b = open("copy1.txt", "r")
e = b.read()
print(e)
a.close()
b.close()
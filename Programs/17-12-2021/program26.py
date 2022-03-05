def stringfun(n):
    if(n[-3:] == "ing"):
        n=n.replace(n[-3:],"ly")
    elif(n[-3:] != "ing"):
        n=n + "ing"
    print("The String after updating is:", n)
n = input("Enter a string:")
stringfun(n);
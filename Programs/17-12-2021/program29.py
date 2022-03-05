def factor(num):
    print("The Factors of", num, "are:")
    for i in range(1, num+1):
        if(num % i == 0):
            print(i)
        i = i + 1

num = int(input("Enter a number to get its factors:"))
factor(num);
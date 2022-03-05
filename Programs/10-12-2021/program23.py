def perfsquare(l, u):
    print("The Perfect square numbers are:")
    for num in (range(l, u)):
        if(num ** (0.5) == int(num ** (0.5)) and num % 2 == 0):
            print(num, end="\t")

l = int(input("Enter lower limit of a 4 digit number:"))
u = int(input("Enter upper limit of a 4 digit number:"))
perfsquare(l, u);
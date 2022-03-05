class Bank:
    def __init__(self, a, n, t, b):
        self.ac = a
        self.name = n
        self.type = t
        self.bal = b
    def deposit(self, d):
        self.bal += d
        print("Now the balance amount is:", self.bal)
    def withdraw(self, w):
        if(self.bal < w):
            print("Not sufficient amount in the account")
        else:
            self.bal -= w
            print("Now the balance amount is:", self.bal)

a = int(input("Enter Account Number:"))
n = input("Enter your Name:")
t = input("Enter Type of Account:")
b = int(input("Enter Balance Amount:"))
obj = Bank(a, n, t, b)
print("Bank Operation")
print("1.Deposit")
print("2.Withdrawal")
print("3.Balance")
opt=int(input("Select your choice:"))
if(opt == 1):
    d = int(input("Enter the Amount to deposit:"))
    obj.deposit(d);
elif (opt == 2):
    w = int(input("Enter the Amount to withdraw:"))
    obj.withdraw(w);
elif (opt == 3):
    print("The balance amount is:", b)
else:
    print("Not Possible")
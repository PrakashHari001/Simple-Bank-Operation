class Bank:
    balance=0
    def __init__(self,amount):
        self.amount=amount
    def deposit(self):
        Bank.balance=Bank.balance+self.amount
        print("Deposit Successful")
        return self.balance
    def withdraw(self):
        if(Bank.balance>=self.amount):
            Bank.balance=Bank.balance-self.amount
            print("Withdraw Susscessful")
            return self.balance
        else:
            print("Insufficient Balance")
            return self.balance
            
print("Initial balance is zero")
opt='y'
while(opt=='y'):
    print("1.Deposit\n2.Withdraw")
    n=int(input("Enter your choice:"))
    if(n==1):
        amount=int(input("Enter amount to be deposited:"))
        dep=Bank(amount)
        bal=dep.deposit()
        print("Balance",bal)
    elif(n==2):
        amount=int(input("Enter amount to be withdraw:"))
        wit=Bank(amount)
        bal=wit.withdraw()
        print("Balance",bal)
    else:
        print("Invalid Option")
    opt=input("Do you want to continue[y/n]:")
    

#Making a Bank Account.
class BankAccount :

    #Defining attributes.
    def __init__(self, name, pin, age) -> None:
        self.name = name 
        self.pin = pin 
        self.age = age
        self.balance = 0
        print(f"\n----------{self.name}----------")

    #Deposit money using this methode.
    def deposit(self, money) :
        self.balance += money
        return f"\n{money}rs Deposit successfully!\nYour new balance : {self.balance}\n"

    #Withdraw money using this methode.
    def withdraw(self, money) :
        if ( self.balance >= money ) :
            self.balance -= money
            return f"Your withdraw amount : {money}.\nYour remaining balance : {self.balance}"
        else : 
            return "You don't have enough money."

    #Know your current balance.
    def current_balance(self) :
        return f"Your current balance is {self.balance}"

#Input detail about the User

my = BankAccount("Priyansh", 13423, 15)

print(my.deposit(10000))
print(my.withdraw(5000))

you = BankAccount("Rahul", 12435, 15)
print(you.deposit(192394))
print(you.deposit(1924))
print(you.withdraw(10000))
import os
import time

current = time.localtime()
current_date = time.strftime("%Y-%m-%d", current)
current_time = time.strftime(" %H:%M:%S", current)

#Making a Bank Account.
class BankAccount :

    #Defining attributes.
    accounts_count = 0

    def __init__(self, name, pin, age) :
        self.name = name 
        self.pin = pin 
        self.age = age
        BankAccount.accounts_count += 1
        if not (os.path.exists(f"{name}_statements.txt")):
            with open(f"{name}_statements.txt", "w") as f:
                pass
        
            with open("Bank Members.txt", "a") as f:
                f.write(f"[{current_date}] {name} [{current_time}]\n")
            
        if not (os.path.exists(f"{name}_balance.txt")):
            with open(f"{self.name}_balance.txt", "w") as f:
                f.write("0")

    def read_balance(self):
        with open(f"{self.name}_balance.txt", "r") as f:
            return float(f.read())

    # Helper method to update the balance in the file
    def update_balance(self, balance):
        with open(f"{self.name}_balance.txt", "w") as f:
            f.write(str(balance))

    def get_amount(self, prompt):
        while True:
            try:
                money = float(input(prompt))
                if money <= 0:
                    print("Amount must be greater than 0.")
                else:
                    return money
            except ValueError:
                print("Enter a proper amount please!")

    #Deposit money using this method.
    def deposit(self) :

        money = self.get_amount("Enter amount to deposit: ")
                
         # Read current balance
        balance = self.read_balance()
        new_balance = balance + money
        self.update_balance(new_balance)

        statement_ask = input("Do you want to add statement (yes/no): ")
        if statement_ask.lower() == "yes":
            statement = input("Add statement: ")
            with open(f"{self.name}_statements.txt", "w") as s:
                s.write(f"[{current_date}] Deposit: {statement} [{current_time}]\n")

        print(f"\n{money}rs Deposit successfully!\n{self.name} new balance : {new_balance}\n")

    #Withdraw money using this methode.
    def withdraw(self) :

        money = self.get_amount("Enter the amount to withdraw: ")
       
        balance = self.read_balance()
        if ( balance >= money ) :
            new_balance = balance - money
            self.update_balance(new_balance)
            statement_ask = input("Do you want to add statement (yes/no): ")
            if statement_ask.lower() == "yes":
                with open(f"{self.name}_statements.txt", "a") as f:
                    statement = input("Add statement: ")
                    f.write(f"[{current_date}] Withdraw: {statement} [{current_time}]\n")
            print (f"{self.name} withdraw amount : {money}.\n{self.name} remaining balance : {new_balance}")
        else : 
            print (f"{self.name} don't have enough money.")

    #Know your current balance.
    def check_balance(self) :
            print(f"{self.name} current balance is {self.read_balance()}")
    
def main():
    name = str(input("Enter your name: "))
    pin = str(input("Enter your pin: "))
    age = str(input("Enter your age: "))
    User = BankAccount(name, pin, age)
    print(f"\n----------{name}----------\n")
    while True:
        option = input("What would you like to do? (Deposit/Withdraw/Check Balance/Exit): ").strip().lower()
        match option:
            case "deposit":
                User.deposit()
            case "withdraw":
                User.withdraw()
            case "check balance":
                User.check_balance()
            case "exit":
                print(f"Thanks for coming {name}!")
                break
            case _:
                print("Invalid option! Try again.")

if __name__ == "__main__":
    main()

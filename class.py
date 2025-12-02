class BankAccount:
    def __init__(self, Account_number, owners_name, date_opened, balance = 0):
        self.account_number = Account_number
        self.balance = balance
        self.owners_name = owners_name
        self.date_opened = date_opened
        print("Welcome")
    def deposit(self, amount):
        if amount < 0:
            print("you can't deposit a negative amount")
        else:
            self.balance += amount
        print(f"You have deposited Ksh. {amount}")
        
    def withdraw(self, amount):
        if self.balance < amount:
            print("insufficient funds")
        else:
            self.balance -= amount
            print(f"You have withdrawn Kshs. {amount}")
                      
    def display_info(self):
          print(f"Your Available Balance is Kshs. {self.balance}")
                    
Account1 = BankAccount("12345", "Henry Mwangi", 2-12-2025, 500)
Account1.deposit(10000)
print(Account1.display_info())                    
                      
        
            
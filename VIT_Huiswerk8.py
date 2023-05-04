
class Account:

    def __init__(self, account_number, owner_name, balance):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    def add_deposit(self, amount):
        self.balance += amount
        print(f"Process completed. New balance: €{self.balance}")
        print(
            f"Account Number: {self.account_number}, Owner Name: {self.owner_name}, Balance: €{self.balance}")

    def withdraw_money(self, amount):
        self.balance -= amount
        print(f"Process completed. New balance: €{self.balance}")
        print(
            f"Account Number: {self.account_number}, Owner Name: {self.owner_name}, Balance: €{self.balance}")

    def total_balance(self):
        print(
            f"Account Number: {self.account_number}, Owner Name: {self.owner_name}, Balance: €{self.balance}")


class Bank:
    BankName = "ING Bank"
    num_clients = 0
    # total_balance = 0

    def __init__(self):
        self.accounts = {}

    def open_account(self, account_number, owner_name, balance):
        self.accounts[account_number] = Account(
            account_number, owner_name, balance)
        print("You have opened a new account. Congratulations 🥳")
        # Bank.total_balance += self.balance
        Bank.num_clients += 1
        print(f"{Bank.num_clients}. musterimizsiniz.")

        # for acc_num, account in bank.accounts.items():
        #     print(
        #         f"Account Number: {acc_num}, Owner Name: {account.owner_name}, Balance: €{account.balance}")

    def del_account(self, account_number):
        del self.accounts[account_number]
        print("The account has been successfully removed.")


bank = Bank()

print("""
88                         88                                 88        
""                         88                                 88        
                           88                                 88        
88 8b,dPPYba,   ,adPPYb,d8 88,dPPYba,  ,adPPYYba, 8b,dPPYba,  88   ,d8  
88 88P'   `"8a a8"    `Y88 88P'    "8a ""     `Y8 88P'   `"8a 88 ,a8"    
88 88       88 8b       88 88       d8 ,adPPPPP88 88       88 8888[       
88 88       88 "8a,   ,d88 88b,   ,a8" 88,    ,88 88       88 88`"Yba,   
88 88       88  `"YbbdP"Y8 8Y"Ybbd8"'  `"8bbdP"Y8 88       88 88   `Y8a  
                aa,    ,88                         
                 "Y8bbdP"                          

Bankacilik sistemine hoş geldiniz!""")

while True:
    choice = input("""  What would you like to do?
    0️⃣   EXIT
    1️⃣   Open an account
    2️⃣   Deposit money
    3️⃣   Withdraw money
    4️⃣   Delete an account
    5️⃣   Total Balance Inquiry
    SECIM: """)

    if choice == "0":
        exit()
    elif choice == "1":
        account_number = input("Please enter new account number?\n")
        owner_name = input("What is your name?\n")
        balance = float(input("What is your balance?\n€"))
        bank.open_account(account_number, owner_name, balance)
    elif choice == "2":
        account_number = input(
            "Please enter account number which you want to deposit money?\n")
        amount = float(input("Please enter the amount.\n€"))
        bank.accounts[account_number].add_deposit(amount)
    elif choice == "3":
        account_number = input(
            "Please enter account number which you want to withdraw money?\n")
        amount = float(input("Please enter the amount.\n€"))
        bank.accounts[account_number].withdraw_money(amount)
    elif choice == "4":
        account_number = input(
            "Please enter account number which you want to remove completely?\n")
        bank.del_account(account_number)
    elif choice == "5":
        account_number = input(
            "Please enter account number which you want to see total balance inquiry?\n")
        bank.accounts[account_number].total_balance()
    else:
        print("Gecersiz bir giris yaptiniz.\nLutfen tekrar deneyin!")

from datetime import datetime
from collections import deque

class Transaction:
    def __init__(self,T_account,Transaction_type,amount,balance):
        d = datetime.now()
        T_date = d.replace(microsecond=0)

        self.T_account = T_account
        self.Transaction_type = Transaction_type
        self.amount = amount
        self.balance = balance
        self.T_date = T_date

        self.log_Transaction()
        if self.Transaction_type == 'Deposit' or self.Transaction_type == 'Withdraw':
            self.User_log_Transaction()

    
    def log_Transaction(self):
        with open("Bank_Transactions.txt", "a") as f:
            f.write(f"{self.T_date} | Acc No.: {self.T_account} - {self.Transaction_type} of Rs.{self.amount} | Balance: Rs.{self.balance}\n")
    
    def User_log_Transaction(self):
        with open(f"User Account Transactions\\{self.T_account}.txt", "a") as f:
            f.write(f"{self.T_date} | {self.Transaction_type} of Rs.{self.amount} | Balance: Rs.{self.balance}\n")


class Accounts:
    def __init__(self, account_no, pin, balance):
        self.Account_no = account_no
        self.Acc_pin = pin
        self.Acc_balance = balance

    def deposit(self,amount):
        if(amount > 0):
            self.Acc_balance += amount
            Transaction(self.Account_no, 'Deposit', amount, self.Acc_balance)
            print(f"Deposited Rs.{amount} to your Account Successfully!")
        else:
            print("Invalid deposit Amount.")

    def withdraw(self,amount):
        if(0 < amount <= self.Acc_balance):
            self.Acc_balance -= amount
            Transaction(self.Account_no, 'Withdraw', amount, self.Acc_balance)
            print(f"Withdrew Rs.{amount} from your Account Successfully!")
        else:
            print("Insufficient funds or Invalid amount.")

    def transfer(self):
        pass

    def check_balance(self):
        amount = 0
        Transaction(self.Account_no, 'Balance Checked', amount, self.Acc_balance)
        return self.Acc_balance

    def mini_statement(self):
        amount = 0
        Transaction(self.Account_no, 'Mini Statment Viewed', amount, self.Acc_balance)

        def statement(num_lines = 5):
            with open(f"User Account Transactions\\{self.Account_no}.txt", "r") as ms:
                last_lines = deque(ms, num_lines)
            return last_lines
        
        last_5_lines = statement(5)

        for line in last_5_lines:
            print(line, end="")

    def qbck(self):
        return self.Acc_balance


class ATM:
    def __init__(self,user_accounts_file):
        self.Accounts_file = user_accounts_file
        self.current_Account = None

    def load_Acc_data(self):
        Bank_Accounts = {}

        with open(self.Accounts_file,"r") as Acc:
            for line in Acc:
                Account_number, pin, balance = line.strip().split(",")
                Bank_Accounts[Account_number] = {
                    "pin" : pin,
                    "balance" : float(balance)
                }
        
        return Bank_Accounts

    def Authenticate_User(self, Account_number, pin):
        Bank_Accounts = self.load_Acc_data()

        if Account_number in Bank_Accounts and Bank_Accounts[Account_number]["pin"] == pin:
            Account_data = Bank_Accounts[Account_number]
            self.current_Account = Accounts(Account_number, pin, Account_data["balance"])
            print("Authentication successful!")
            print("Welcome User!")
            return True
        print("Authentication Failed, Please check your account number and PIN.")
        return False

    def Update_Acc_data(self):
        Bank_Accounts = self.load_Acc_data()

        Bank_Accounts[self.current_Account.Account_no]["balance"] = self.current_Account.qbck()

        with open(self.Accounts_file,"w") as updata:
            for Account_number, data in Bank_Accounts.items():
                updata.write(f"{Account_number},{data['pin']},{data['balance']}\n")

    def Perform_Actions(self, Action, amount = 0):
        if Action == "check-balance":
            print(f"Your current balance is: Rs.{self.current_Account.check_balance()}")
        elif Action == "deposit":
            self.current_Account.deposit(amount)
            self.Update_Acc_data()
        elif Action == "wd":
            self.current_Account.withdraw(amount)
            self.Update_Acc_data()
        elif Action == "MS":
            self.current_Account.mini_statement()
        else:
            print("Invalid Input")

    def logout(self):
        self.current_Account = None
        print("Logged out. Thank you for using our ATM.")


def ATM_main():

    atm = ATM("Accounts.txt")

    print("Welcome to XYZ ATM!")
    account_number = input("Enter your Account Number: ")
    pin = input("Enter your ATM PIN: ")
    print()

    if atm.Authenticate_User(account_number,pin):
        while True:
            print("\nChoose an option:")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Mini Statement")
            print("5. Exit")
            option = int(input("Select an option: "))

            if option == 1:
                atm.Perform_Actions("check-balance")

            elif option == 2:
                amount = float(input("Enter Amount to Deposit: "))
                atm.Perform_Actions("deposit",amount)

            elif option == 3:
                amount = float(input("Enter Amount to Withdraw: "))
                atm.Perform_Actions("wd",amount)

            elif option == 4:
                atm.Perform_Actions("MS")

            elif option == 5:
                atm.logout()
                break

            else:
                print("Invalid option. Try again.")


ATM_main()


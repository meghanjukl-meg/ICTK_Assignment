class Bank_Account:
    def __init__(self):

        self.balance = 0

    def deposit(self):
        amount = float(input("Enter amount to be deposited :"))
        self.balance += amount
        print(f"Successfully deposited Rs.{amount}")

    def withdraw(self):
        amount = float(input("Enter amount to withdraw"))
        if amount <= self.balance:
            self.balance -= amount
            print(f"you have successfully withdrawn Rs.{amount}")
        else:
            print("Not enough money to withdraw")

    def balance_check(self):
        print(f"Available Balance = {self.balance}")


account_no = 45678
account_number = int(input("Enter account number :"))
if account_number== account_no:
    print("choose your type of transaction:/n"
          "1.Deposit"
          "2.Withdrawal"
          "3.Check Balance/n")
    option=int(input("Enter your choice 1/2/3"))

    account = Bank_Account()
    if option == 1:
        account.deposit()
    elif option ==2:
        account.withdraw()
    else:
        account.balance_check()
else:
    print("Invalid Account Number")
class Person:
    def _init_(self, first_name, middle_name, last_name, bank_accounts):
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.bank_accounts = bank_accounts

class BankAccount:
    def __init__ (self, user, account_type, balance, status):
        self.user = user
        self.account_type = account_type
        self.balance = balance
        self.status = status

    def transfer(self, amount, toAccount):
        toAccount.balance = amount
        print("Currently transferring...")

customer1 = BankAccount("WReading" , "Checking" , 100, ["open"])
customer1.transfer(70, 30)


checking_account = BankAccount("Customer" , "Checking", 100, ["open"])
print(checking_account)
print(checking_account.user.first_name)
print(checking_account.user.first_name)


checking_account.transfer(120, "Savings")
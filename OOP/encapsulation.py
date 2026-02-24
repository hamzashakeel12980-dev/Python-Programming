class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    def deposit(self, amount):
        self.__balance += amount
    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds")
        else:
            self.__balance -= amount
    def get_balance(self):
        return self.__balance
account = BankAccount(9000)
account.deposit(1500)
account.withdraw(2000)
print("Current balance:", account.get_balance())
# --- IGNORE ---
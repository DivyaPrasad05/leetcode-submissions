class Bank:

    def __init__(self, balance: List[int]):
        self.balance = balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        # checker to ensure that the account1 id exists
        if not self.checkAccountID(account1):
            return False
        
        # checker to ensure that the account2 id exists
        if not self.checkAccountID(account2):
            return False
        
        # withdraw from account 1
        wd = self.withdraw(account1, money)
        if not wd:
            return False

        # deposit to account 2
        dep = self.deposit(account2, money)
        if not dep:
            return False

        return True

    def deposit(self, account: int, money: int) -> bool:
        # checker to ensure that the account id exists
        if not self.checkAccountID(account):
            return False

        # deposit the money in the account
        self.balance[account - 1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        # checker to ensure that the account id exists
        if not self.checkAccountID(account):
            return False
        # checker to ensure that the balance is 0 or pos
        isPos = self.balance[account - 1] - money

        if isPos >= 0:
            self.balance[account - 1] -= money
            return True
        else:
            return False # transaction didnt go thru

    def checkAccountID(self, account):
        return False if account > len(self.balance) else True

# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
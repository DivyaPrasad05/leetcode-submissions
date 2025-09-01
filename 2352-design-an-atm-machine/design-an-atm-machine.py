class ATM:

    def __init__(self):
        # k: bills, v: counts
        self.den = [20, 50, 100, 200, 500]
        self.counts = [0] * 5

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(len(banknotesCount)):
            self.counts[i] += banknotesCount[i]

    def withdraw(self, amount: int) -> List[int]:
        res = [0] * 5

        for i in range(len(self.den) - 1, -1, -1):
            used = min(amount // self.den[i], self.counts[i])
            res[i] = used
            amount -= used * self.den[i]
        
        if amount != 0:
            return [-1]
        
        # update the counts and do actual withdrawal
        for i in range(len(self.counts)):
            self.counts[i] -= res[i]
        return res
        

# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)
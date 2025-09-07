class Solution:
    def fib(self, n: int, memo = {}) -> int:
        # memo -> k: n, val: fib #
        if n in memo:
            return memo[n]
        if n < 2:
            return n
        else:
            memo[n] = self.fib(n - 1, memo) + self.fib(n - 2, memo)
            return memo[n]
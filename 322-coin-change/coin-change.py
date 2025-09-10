class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        
        # DP table
        dp = [0] * (amount + 1)

        for i in range(1, amount + 1):
            minAmt = float('inf')

            for coin in coins:
                diff = i - coin
                if diff < 0:
                    break
                minAmt = min(minAmt, dp[diff] + 1)
            
            dp[i] = minAmt

        if dp[amount] < float('inf'):
            return dp[amount]
        else:
            return -1
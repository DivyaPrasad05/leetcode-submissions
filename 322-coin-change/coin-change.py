class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        memo = {0:0}

        def minCoins(amt):
            # Base Case:
            if amt in memo:
                return memo[amt]
            
            minAmt = float('inf')
            for coin in coins:
                diff = amt - coin
                if diff < 0:
                    break
                minAmt = min(minAmt, 1 + minCoins(diff))

            memo[amt] = minAmt
            return minAmt
        
        res = minCoins(amount)
        if res < float('inf'):
            return res
        else:
            return -1
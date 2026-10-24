# Runtime: 1243 ms
# Memory: 133.1 MB

import sys
sys.setrecursionlimit(20000)

class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        if amount == 0:
            return 0
        if not coins:
            return -1
        dp = [[-1] * (amount + 1) for _ in range(len(coins))]
        def f(i: int, rem: int) -> float:
            if rem == 0:
                return 0
            if rem < 0 or i >= len(coins):
                return float('inf')
            if dp[i][rem] != -1:
                return dp[i][rem]
            tk = 1 + f(i, rem - coins[i])
            nt = f(i + 1, rem)
            dp[i][rem] = min(tk, nt)
            return dp[i][rem]
        ans = f(0, amount)
        return ans if ans != float('inf') else -1
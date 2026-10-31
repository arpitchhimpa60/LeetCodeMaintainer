# Runtime: 10 ms
# Memory: 20.7 MB

class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)
        dp =[-1] * (n)
        def f(i):
            if i>=n:
                return 0
            if dp[i]!=-1: return dp[i]
            nt = f(i+2) + cost[i]
            tk = cost[i] + f(i+1)
            dp[i] = min(tk,nt)
            return dp[i]
        return min(f(0),f(1))
        
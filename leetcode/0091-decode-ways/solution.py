# Runtime: 2 ms
# Memory: 19.5 MB

class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [-1] * (len(s))
        def f(i):
            if i>=len(s): return 1
            if dp[i]!=-1: return dp[i]
            ways = 0
            if s[i]!="0": ways+=f(i+1)
            if i+1 < len(s) and "10"<=s[i:i+2]<="26": ways+=f(i+2)
            dp[i] = ways
            return dp[i]
        return f(0)
        
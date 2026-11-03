# Runtime: 0 ms
# Memory: 19.5 MB

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[-1]*n for _ in range(m)]
        dp[m-1][n-1] = 1
        def f(i,j):
            if i>=m or j>=n or i<0 or j<0:
                return 0
            if obstacleGrid[i][j]==1:
                return 0
            if dp[i][j]!=-1: return dp[i][j]
            right = f(i,j+1)
            down = f(i+1,j)
            dp[i][j] = right+down
            return dp[i][j]
        return f(0,0)
        
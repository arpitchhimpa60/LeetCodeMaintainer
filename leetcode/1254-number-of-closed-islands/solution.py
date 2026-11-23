# Runtime: 19 ms
# Memory: 20.5 MB

class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        m = len(grid[0])
        n = len(grid)
        adj = [[False]*m for _ in range(n)]
        count = 0
        def dfs(i,j):
            if i<0 or i>=n or j<0 or j>=m or adj[i][j] or grid[i][j] == 1:
                return
            
            adj[i][j] = True
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)

        for i in range(n):
            for j in range(m):
                if (i == 0 or i == n - 1 or j == 0 or j == m - 1) and grid[i][j] == 0 and not adj[i][j]:
                    dfs(i, j)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0 and not adj[i][j]:
                    count += 1
                    dfs(i, j)
        return count


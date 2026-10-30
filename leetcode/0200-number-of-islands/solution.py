# Runtime: 255 ms
# Memory: 22.1 MB

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid[0])
        n = len(grid)
        adj = [[False]*m for _ in range(n)]
        count = 0
        def dfs(i,j):
            if i<0 or i>=n or j<0 or j>=m or adj[i][j] or grid[i][j] == '0':
                return 
            adj[i][j] = True
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1' and not adj[i][j]:
                    count+=1
                    dfs(i,j)
        return count

        
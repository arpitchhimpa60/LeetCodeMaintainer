# Runtime: 2 ms
# Memory: 20.2 MB

class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]<0:
                    cnt+=1
        return cnt

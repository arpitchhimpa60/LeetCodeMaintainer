# Runtime: 106 ms
# Memory: 32 MB

class Solution:
    def maxIceCream(self, costs: list[int], coins: int) -> int:
        costs.sort()
        cnt = 0
        i = 0
        n = len(costs)
        while coins>0:
            if coins>=costs[i]:
                coins-=costs[i]
                cnt+=1
            i+=1
            if i>=n:
                return cnt
        return cnt
            

        
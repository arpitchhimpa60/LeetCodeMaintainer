# Runtime: 327 ms
# Memory: 32.6 MB

class Solution:
    def halveArray(self, nums: list[int]) -> int:
        total = sum(nums)/2
        import heapq
        heap = [-x for x in nums]
        heapq.heapify(heap)
        # print(heap)
        cnt = 0
        diff = -sum(heap)
        while diff > total:
            val = -heapq.heappop(heap)
            while diff > total:
                red = val/2
                diff -= red
                val = val/2
                cnt+=1
                if heap and val <= -heap[0]:
                    break
            heapq.heappush(heap,-val)
        return cnt

        
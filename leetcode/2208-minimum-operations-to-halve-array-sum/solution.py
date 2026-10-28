# Runtime: 280 ms
# Memory: 32.4 MB

class Solution:
    def halveArray(self, nums: list[int]) -> int:
        import heapq
        heap = [-x for x in nums]
        heapq.heapify(heap)
        original_sum = sum(nums)
        curr_sum = original_sum
        cnt = 0
        while curr_sum > original_sum /2:
            cnt+=1
            maxi = -heapq.heappop(heap)
            curr_sum -= maxi/2
            heapq.heappush(heap,-maxi/2)
        return cnt
        

        
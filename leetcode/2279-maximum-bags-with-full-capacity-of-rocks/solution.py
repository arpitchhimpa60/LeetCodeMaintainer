# Runtime: 126 ms
# Memory: 29.2 MB

class Solution:
    def maximumBags(self, capacity: list[int], rocks: list[int], additionalRocks: int) -> int:
        import heapq
        heap = []
        for i in range(len(capacity)):
            heap.append(abs(capacity[i]-rocks[i]))
        heapq.heapify(heap)
        cnt = 0
        print(heap)
        while heap:
            x = heapq.heappop(heap)
            if x==0:
                cnt+=1
                continue
            if additionalRocks >= x:
                additionalRocks -= x
                cnt+=1
        return (cnt)
        
# Runtime: 223 ms
# Memory: 44.5 MB

class Solution:
    def minSetSize(self, arr: list[int]) -> int:
        dic = {}
        for i in arr:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        n = len(arr)
        import heapq
        heap = [[-dic[i],i] for i in dic]
        heapq.heapify(heap)
        # print(heap)
        total = 0
        cnt = 0
        while heap:
            start, end = heapq.heappop(heap)
            if total>=(n/2):
                break
            total+=(-start)
            cnt+=1
        return cnt



            
            
        
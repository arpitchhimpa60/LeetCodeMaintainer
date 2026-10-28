# Runtime: 8 ms
# Memory: 20 MB

class Solution:
    def frequencySort(self, s: str) -> str:
        dic = {}
        for i in s:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        arr=[[dic[x],x] for x in dic]
        heapq.heapify(arr)
        res = []
        while len(arr):
            temp = heapq.heappop(arr)
            res.append(temp[1]*temp[0])
        return ("".join(res[::-1]))
        
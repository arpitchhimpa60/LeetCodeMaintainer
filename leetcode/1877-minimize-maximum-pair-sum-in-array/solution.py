# Runtime: 877 ms
# Memory: 33.3 MB

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        j = len(nums)-1
        mx = 0
        while i<j:
            mx = max(mx,nums[i]+nums[j])
            i+=1
            j-=1
        return mx
        
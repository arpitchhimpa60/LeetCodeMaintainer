# Runtime: 18 ms
# Memory: 24.8 MB

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        val = 1
        cnt = 0
        for i in nums:
            if i!=0:
                val *= i
            else:
                cnt+=1
        if cnt >1:
            arr = [0] * len(nums)
            return arr
        for i in range(len(nums)):
            if cnt==1:
                if nums[i]!=0:
                    nums[i] = 0
                else:
                    nums[i] = val
            elif nums[i]==0:
                nums[i] = val
            else:
                nums[i] = int(val // nums[i])
        return nums
        
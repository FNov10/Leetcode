class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # a subarray would be (R-L)+1
        currMin = float('inf')
        currSum = 0
        L = 0
        for R, value in enumerate(nums):
            currSum += value
            while currSum>=target:
                currMin = min(currMin, R-L+1)
                currSum-=nums[L]
                L+=1
                
        if currMin == float('inf'):
            return 0
        return currMin
            

        
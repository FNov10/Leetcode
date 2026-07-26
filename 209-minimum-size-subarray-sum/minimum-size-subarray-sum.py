class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L, R = 0, 0
        currSum = 0
        minLen = float('inf')
        while R<len(nums) :
            currSum+=nums[R]
            while currSum >=target and L<=R:
                length = R-L + 1
                minLen = min(length, minLen)
                currSum-=nums[L]
                L+=1
            R+=1
        if minLen == float('inf'):
            return 0
        return minLen

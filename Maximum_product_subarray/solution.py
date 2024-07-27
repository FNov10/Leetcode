""" How it works???
- We store the local max and local min at each step to account for next iteration being a different sign
- at next iteration, we compute local max and local min using both previous local max and local min
    - 4 different variables
- new local max is max of all these
- new local min is min of all these. """

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        globalMax = float('-inf')
        for index in range(len(nums)):
            if index == 0:
                localMax = nums[index]
                localMin = nums[index]
            else:
                maxVal = max(nums[index],nums[index]*localMax)
                minVal = min(nums[index],nums[index]*localMax)
                maxVal1 = max(nums[index],nums[index]*localMin)
                minVal1 = min(nums[index],nums[index]*localMin)
                localMax = max(maxVal,minVal,minVal1,maxVal1)
                localMin = min(maxVal,minVal,minVal1,maxVal1)
            globalMax = max(globalMax,localMax)
        return globalMax
        

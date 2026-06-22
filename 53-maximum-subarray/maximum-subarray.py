class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadanes algorithm
        maxSum = nums[0]
        currSum = 0
        for n in nums:
            currSum = max(0, currSum)
            currSum += n
            maxSum = max(currSum, maxSum)
        return maxSum

        
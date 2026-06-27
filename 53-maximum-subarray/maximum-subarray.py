class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float('-inf')
        currSum = 0
        for n in nums:
            currSum = max(0, currSum)
            currSum+=n
            maxSum = max(maxSum, currSum)
        return maxSum
        
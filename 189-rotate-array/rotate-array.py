class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        numscopy = nums.copy()
        for index, value in enumerate(numscopy):
            newindex = index + k
            while newindex >= len(nums):
                newindex = newindex - len(nums)
            if newindex <len(nums):
                 nums[newindex] = value
        
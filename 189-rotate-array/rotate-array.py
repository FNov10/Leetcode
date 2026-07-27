class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k == 0 :
            return nums

        copy = nums.copy()
        for index, value in enumerate(copy):
            if index + k < len(nums):
                newindex = index+k
                nums[newindex] = value
            else:
                newindex =  (index+k) - len(nums)
                while not 0<=newindex<len(nums):
                    newindex-=len(nums)
                nums[newindex]=value
        
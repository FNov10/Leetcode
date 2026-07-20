class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = set()
        for index, value in enumerate(nums):
            if index>0 and value == nums[index-1]:
                continue
            L = index+1
            R = len(nums)-1
            target = 0 - value
            while L<R:
                if nums[R] + nums[L] == target:
                    res.add((value,nums[L],nums[R]))
                    R-=1
                elif nums[R]+nums[L]< target:
                    L+=1
                else:
                    R-=1
        final = []
        for tup in res:
            final.append(list(tup))
        return final



        
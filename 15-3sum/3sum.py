class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        final = set()
        for index, num in enumerate(nums):
            
            L = index+1
            R = len(nums)-1
            target = num*-1
            while L<R and L<len(nums):
                total = nums[L] + nums[R]
                if total == target and total not in final:
                    final.add((num,nums[R],nums[L]))
                    R-=1
                elif total < target:
                    L+=1
                else:
                    R-=1
        finalfinal = []
        for hashset in final:
            finalfinal.append(list(hashset))
        return finalfinal


        
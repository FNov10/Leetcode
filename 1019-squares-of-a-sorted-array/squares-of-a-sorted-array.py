class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        L, R = 0, len(nums)-1
        final = []
        while L<=R:
            if abs(nums[R])>abs(nums[L]):
                final.append(nums[R]**2)
                R-=1
            else:
                final.append(nums[L]**2)
                L+=1
        final.reverse()
        return final
        
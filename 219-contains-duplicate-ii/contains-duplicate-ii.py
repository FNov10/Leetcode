from collections import Counter
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = {nums[0]}
        L, R = 0, 1
        while R<len(nums):
            while abs(R-L)>k:
                window.remove(nums[L])
                L+=1
            if nums[R] in window:
                return True
            window.add(nums[R])
            R+=1
        return False



        
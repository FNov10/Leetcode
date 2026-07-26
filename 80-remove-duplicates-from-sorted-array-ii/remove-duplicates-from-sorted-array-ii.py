from collections import Counter
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        trueIndex = 0
        window = {}
        for n in nums:
            if window.get(n, 0) < 2:
                window[n] = window.get(n, 0) + 1
                nums[trueIndex] = n
                trueIndex+=1
        return trueIndex

            
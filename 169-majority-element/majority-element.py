from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counterr = Counter(nums)
        return max(counterr, key=counterr.get)
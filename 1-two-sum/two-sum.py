class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index, value in enumerate(nums):
            needed = target - value
            if needed in seen:
                return [index, seen[needed]]
            seen[value] = index
        
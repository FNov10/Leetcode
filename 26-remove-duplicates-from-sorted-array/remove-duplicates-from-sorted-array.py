class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        window = set()
        trueIndex = 0
        for n in nums:
            if n not in window:
                nums[trueIndex ] = n
                window.add(n)
                trueIndex+=1

        return trueIndex
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        trueIndex = 0
        for n in nums:
            if n != val:
                nums[trueIndex] = n
                trueIndex+=1
        return trueIndex
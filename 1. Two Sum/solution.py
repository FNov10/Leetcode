class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myDict = {}
        for num in nums:
            myDict[num] = target - num
        for num in myDict:
            if (myDict[num] in nums):
                if nums.count(num) >1:
                    indexA=nums.index(num)
                    nums.remove(num)
                    indexB=nums.index(num)+1
                    return [indexA,indexB]
                elif myDict[num] != num:
                    return [nums.index(num),nums.index(myDict[num])]

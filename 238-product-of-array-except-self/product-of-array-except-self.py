class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixArray = self.prefixSum(nums)
        postfixArray = self.prefixSum(nums[::-1])[::-1]
        output = []
        for index, num in enumerate(nums):
            output.append(prefixArray[index] * postfixArray[index])
        return output
        
    def prefixSum(self, numss):
        currPrefix = 1
        final = []
        for index, value in enumerate(numss):
            final.append(currPrefix)
            currPrefix*=value
        return final

        
        
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        currL = 1
        L = []
     
        for n in nums:
            L.append(currL)
            currL = n*currL
        reverse = nums[::-1]
        currR = 1
        R = []
        for n in reverse:
            R.append(currR)
            currR = n * currR
        R = R[::-1]
        result = []
        for i in range(len(nums)):
            result.append(L[i]*R[i])
        return result
        

        
        
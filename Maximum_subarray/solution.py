""" Kadanes algorithm for Maximum contiguous subarray
	Instead of looking at brute force as naive way, try to think of it as local maximums.
	Max of all local maximums is the answer.
	Computing the local maximums as you go is the key. Since they do not need to be re-computed.
	Top down DP approach
	
	example - [1,2,-3,4,5,6,7]
		Local max at index i = max of all the subarrays that contain index 2, to the left of 2
		Local max at i+1 = max(arr[i] itself, arr[i+1] + localMax(i))
		
	Lets say LocalMax at index 1:
		[1,2], [2] , Localmax = 3
	LocalMax at index 2:
		[1,2,-3],[2,-3],[-3] 
		
	Notice how the first two subarrays are the same as the subarrays at index 1, with the added i
	Based on mathematical logic, the max considernig just those two subarrays, is the same as the local maxx at index 1, but just adding -3
	Our next unaccounted for item is just [-3] on its own
	So we have two computations, localMax at index 1 + index 2, and index 2 on its own, max of these is our next localmax
		
	KEY IS LOCAL MAX BEING COMPUTED. DP APPROACH!!! """

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxx = float('-inf')
        for index in range(len(nums)):
            if index == 0:
                localMax = nums[index]
            else:
                localMax = max(nums[index], localMax+nums[index])
            maxx = max(localMax,maxx)

        return maxx
    

""" 
  Explanation: Modified binary search 
  start with l,r,mid pointers as usual
  if left < mid , means we are in the sorted portion:
    scan regular binary search on left side
    if not found, scan right half
  MAIN CONCEPT: doing regular binary search over and over, only for sorted portions of the


 """



class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left<=right:
            mid =left + (right - left) // 2

            if target == nums[mid]:
                return mid
            if nums[left]<=nums[mid]:
                if nums[left]<=target<=nums[mid]:
                    right = mid -1
                else:
                    left = mid +1
            else:
                if nums[mid]<=target<=nums[right]:
                    left = mid + 1
                else:
                    right = mid -1
        return -1

        
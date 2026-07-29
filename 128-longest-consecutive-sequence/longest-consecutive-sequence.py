class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        longest = 1
        hashset = set(nums)
        for num in hashset:
            if num-1 not in hashset and num+1 in hashset:
                # now at minumum
                length = 1
                while num + length in hashset:
                    length+=1
                longest = max(longest, length)
            else:
                continue
        return longest
            
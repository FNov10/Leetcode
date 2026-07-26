class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        L, R = 0, 0
        finalSet = set()
        maxLen = float('-inf')
        for R, value in enumerate(s):
            while value in finalSet:
                finalSet.remove(s[L])
                L+=1
            finalSet.add(value)
            maxLen = max(maxLen, len(finalSet))
        return maxLen
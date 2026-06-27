class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        window = set()
        currLen = 0
        maxLen = float('-inf')
        L = 0
        for R, value in enumerate(s):
            while value in window:
                window.remove(s[L])
                L+=1
                currLen-=1
            window.add(value)
            currLen+=1
            maxLen = max(currLen, maxLen)
        return maxLen
        
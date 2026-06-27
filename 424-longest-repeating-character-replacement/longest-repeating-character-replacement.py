from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLen = 0
        L = 0
        R = 0
        windowHash = {letter: 0 for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}
        currLen = 0
        for R, value in enumerate(s):
            windowHash[value]+=1
            currLen += 1
            while ((currLen - max(windowHash.values())) > k) and L<=R:
                windowHash[s[L]]-=1
                L+=1
                currLen-=1
            maxLen = max(currLen, maxLen)
        return maxLen
    
            
        
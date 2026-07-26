class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s)==1: return 1
        L, R = 0, 0
        counterSet = {"start":0}
        maxLen = float('-inf')
        while R<len(s):
            counterSet[s[R]] = counterSet.get(s[R], 0) + 1
            while (R-L)+1 - max(counterSet.values()) > k:
                counterSet[s[L]] -= 1
                L+=1
            currLen = (R-L)+1
            maxLen = max(maxLen, currLen)
            
            R+=1
        return maxLen

        
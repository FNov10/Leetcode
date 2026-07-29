class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        final = ''
        i = 0
        j = 0
        while i<len(s) and j<len(t):
            if s[i] == t[j]:
                final+=s[i]
                i+=1
                j+=1
            else:
                j+=1
        return final==s
        
        
        
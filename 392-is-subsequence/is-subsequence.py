class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        i, j = 0, 0
        final = []
        while i<len(s) and j<len(t):
            if s[i] == t[j]:
                final.append(s[i])
                i+=1
            j+=1
        return ''.join(final)==s
            
        
        
        
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        if len(s)>len(t):
            return False
        if s==t:
            return True
        i, j = 0, 0
        final = ""
        while i<len(s) and j<len(t):
            
            if s[i] == t[j]:
                final+=t[j]
                i+=1
            j+=1
        return final==s
            
        
        
        
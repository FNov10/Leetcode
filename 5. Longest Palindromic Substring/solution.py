class Solution:
    def longestPalindrome(self, s: str) -> str:
        reslen = 0
        res = []
        for i in range(len(s)):
            #odd
            L,R = i,i
            while L>=0 and R<len(s) and s[L] == s[R]:
                if (R-L+1) >= reslen:
                    reslen = R-L+1
                    res =[L,R]
                L-=1
                R+=1
            
            #even
            L,R = i,i+1
            while L>=0 and R<len(s) and s[L] == s[R]:
                if (R-L+1) >= reslen:
                    reslen = R-L+1
                    res = [L,R]
                L-=1
                R+=1

        return s[res[0]:res[1]+1]
        
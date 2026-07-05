class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = len(s1)-1
        L = 0
        R = window
        
        while R<len(s2):
            if sorted(s2[L:R+1]) == sorted(s1):
                return True
            L+=1
            R= L + window
        return False
        
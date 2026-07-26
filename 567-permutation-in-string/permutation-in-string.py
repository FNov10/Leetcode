from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = len(s1) -1
        s1Counter = Counter(s1)
        for index in range(len(s2) - window):
            s2sub = Counter(s2[index:index+len(s1)])
            if s1Counter == s2sub:
                return True
        return False

        
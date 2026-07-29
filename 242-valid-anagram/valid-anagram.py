from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = re.sub(r'[^A-Za-z]','',s).lower()
        t = re.sub(r'[^A-Za-z]','',t).lower()
        return Counter(s)==Counter(t)
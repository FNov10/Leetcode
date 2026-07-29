from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counterRansom = Counter(ransomNote)
        counterMagazine = Counter(magazine)

        for letter, count in counterRansom.items():
            if count>counterMagazine[letter]:
                return False
        return True
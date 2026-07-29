class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern = list(pattern)
        s = s.split()
        if len(s)!=len(pattern): return False
        hashmap = {}
        for index, letter in enumerate(pattern):
            if letter in hashmap:
                if hashmap[letter] != s[index]:
                    return False
            elif s[index] in hashmap.values():
                return False
            else:
                hashmap[letter] = s[index]
        return True

        
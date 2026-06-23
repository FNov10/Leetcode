class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        hashmap = dict()
        s = s.split()
        if len(pattern) != len(s):
            return False
        for index in range(len(pattern)):
            if pattern[index] not in hashmap:
                if s[index] in hashmap.values():
                    return False
                hashmap[pattern[index]] = s[index]
            elif hashmap[pattern[index]] != s[index]:
                return False
        return True

        
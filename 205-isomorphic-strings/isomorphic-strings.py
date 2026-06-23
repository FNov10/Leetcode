class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashmap = {}
        for index in range(len(s)):
            if s[index] not in hashmap:
                if t[index] in hashmap.values():
                    return False
                hashmap[s[index]] = t[index]
            elif hashmap[s[index]] != t[index] :
                return False
        return True


        
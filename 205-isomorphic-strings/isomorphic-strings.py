class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashmap = {}
        for index, letter in enumerate(s):
            if letter in hashmap:
                if hashmap[letter]!=t[index]:
                    return False
            elif t[index] in hashmap.values():
                return False
            else:
                hashmap[letter] = t[index]
        return True


        
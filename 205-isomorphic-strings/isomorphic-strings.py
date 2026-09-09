class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        solution = {}
        for index in range(len(s)):
            if s[index] in solution:
                if t[index] != solution[s[index]]:
                    return False
            elif t[index] in solution.values():
                if s[index] not in solution:
                    return False
            solution[s[index]] = t[index]
        return True
        
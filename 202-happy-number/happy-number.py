class Solution:
    def isHappy(self, n: int) -> bool:
        res = {1,0}
        seen = set()
        found = False
        while not found:
            if n in seen:
                return False
            seen.add(n)
            x= (sum([int(element)**2 for element in str(n)]))
            n = x
            if n ==1:
                found= True
        return found

        
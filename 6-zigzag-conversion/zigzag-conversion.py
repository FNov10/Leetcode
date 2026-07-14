class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        i = 0
        d = 1
        sol = [[] for blah in range(numRows)]

        for char in s:
            sol[i].append(char)
            if i ==0:
                d = 1
            elif i == numRows-1:
                d = -1
            i+=d
        final = ""
        for row in sol:
            final+=''.join(row)
        return final


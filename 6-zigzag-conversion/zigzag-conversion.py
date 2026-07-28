class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        matrix = [[] for row in range(numRows)]
        rowindex = 0
        d = 1
        for letter in s:
            matrix[rowindex].append(letter)
            if rowindex == 0:
                d = 1
            elif rowindex == len(matrix)-1:
                d = -1
            rowindex +=d
        final = ""
        for row in matrix:
            final+=''.join(row)
        return final

            


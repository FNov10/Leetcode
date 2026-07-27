class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        R = len(s)-1
        finalIndex = 0
        while R>=0 and not re.match( r'[A-Za-z]', s[R]):
            R-=1

        # Now, we reached a non whitespace. This is our last word
        counter = 0

        while R>=0 and re.match(r'[A-Za-z]',s[R]):
            counter+=1
            R-=1
        return counter
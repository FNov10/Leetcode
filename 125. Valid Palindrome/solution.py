#O(N) solution :)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        return self.extract_extras(self.reverse_string(s))==self.extract_extras(s)

    #Using python isalnum() method to extract alphanumerics
    #O(n)
    def extract_extras(self, s: str) -> str:
        self.s = s.lower()
        final = ''
        for char in self.s:
            if char.isalnum():
                final+=char
        return final

    #reverse string (o(n))
    def reverse_string(self,s: str):
        reversed = ''
        for char in s:
            reversed = char + reversed
        return reversed
        
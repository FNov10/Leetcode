class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needlength = len(needle)
        if len(needle)>len(haystack):
            return -1
        for index in range(0, len(haystack)-needlength+1):
            if haystack[index:index+needlength] == needle:
                return index
        return -1
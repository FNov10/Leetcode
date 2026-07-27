class Solution:
    def romanToInt(self, s: str) -> int:
        SpecialMap = {
            "IV": 4, "IX": 9,
            "XL":40, "XC":90,
            "CD":400, "CM":900
        }
        RegularMap = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        final = 0
        for roman, integer in SpecialMap.items():
            if roman in s:
                s = s.replace(roman,"")
                final+=integer
        for roman in s:
            final+=RegularMap[roman]
        return final

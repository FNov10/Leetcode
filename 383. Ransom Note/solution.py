class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        #creating hashmap
        ranshash=Counter(ransomNote)
        maghash=Counter(magazine)

        #Loop through each letter
        count = 0
        for letter in ransomNote:
            #if for each letter in ransom, there is a corresponding hash map in maghash,    increment
            if (letter in maghash.keys()) :
                if (maghash[letter]>=ranshash[letter]):
                    count+=1
        return count==len(ransomNote)

        
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #Sliding window technique
        hash ={}
        L = 0
        maxx = 0
        for R in range(len(s)):
            #Hash table with counter of every substring
            hash[s[R]] = 1+ hash.get(s[R],0)

            #copy made as hash table modifies in for loop
            x = hash.copy().values()
            for num in x:
                #if our substring has a letter more than one occurence, move left pointer to right
                    #and if that removed letter from substring is 0 occurence, remove it from dict. this is done as our maxx is calculated as len of hash, having a 0 makes len incorrect
                if num>1:
                    hash[s[L]]-=1
                    if hash[s[L]] ==0:
                        del hash[s[L]]
                    L+=1
            else:
                #if this block is hit, all hash values are one. Meaning every letter in substring apepars once
                #so len of dict is len of substring
                #max to see longest substring
                maxx = max(maxx,len(hash))
        return maxx
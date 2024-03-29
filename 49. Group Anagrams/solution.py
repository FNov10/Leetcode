class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        index=0
        hashmap = {}
        #leaves us with hashmap as follows {0:'aet',1:'aet'}
        for str in strs:
            hashmap[index] = ''.join(sorted(str))
            index+=1
        flipped = {}

        #finding keys with duplicate values. These duplicate values represent the anagrams
        #the keys represent the index
        #leaves us with a dict as follows {'aet':[0,1,3]}
        for key,value in hashmap.items():
            if value not in flipped:
                flipped[value] = [key]
            else:
                flipped[value].append(key)

        #Loop through the dictionary indices and assign them to corresponding strs index
        #keep in mind , every value in the flipped dict is an array of indices containing the anagrams
        final =[]
        ind = 0
        for indices in flipped.values():
            group = []
            for index in indices:
                group.append(strs[index])
            final.append(group)
                
        return final
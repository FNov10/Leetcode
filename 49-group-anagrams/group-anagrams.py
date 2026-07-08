class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final_dict = {}
        for word in strs:
            sortedword = ''.join(sorted(word))
            if sortedword in final_dict:
                final_dict[sortedword].append(word) 
            else:
                final_dict[sortedword] = [word]

        final = []
        for wordlist in final_dict.values():
            final.append(wordlist)
        return final

        
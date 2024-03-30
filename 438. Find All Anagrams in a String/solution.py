class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        #This solution loops through each slice of s, checks if hashmap of sliced window equals hashmap of p
        an_len = len(p)
        start_index = 0
        s_hash = Counter(p)
        output = []
        while start_index<=(len(s)-an_len):
            window = s[start_index:start_index+an_len]
            hash = Counter(window)
            if hash==s_hash:
                output.append(start_index)
            start_index+=1
        return output

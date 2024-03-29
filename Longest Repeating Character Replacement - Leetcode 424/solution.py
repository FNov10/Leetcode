from collections import Counter

#Submitted solution
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L = 0
        R=0
        maxx = 0
        counter = {}
        while (L<=R) & (R<len(s)):
            #Getting hashmap of window frequency (window is the slice) on the fly
            counter[s[R]] = 1+counter.get(s[R],0) #Alternative would be to use Counter on the window and slice, but complexity greatly suffers.

            #window length - +1 to account for index
            window = (R-L)+1
            #get most frequent character
            mostFreq = max(counter.values())
            #Window length minus mostFreq gives us the number of characters to be swapped
            rest = window-mostFreq

            #If rest is less than k, all the rest of letters can be swapped out. Adding the rest and most frew gives us the length of the final string
            #alternatively, window length can also be used. 
            if rest<=k:
                R+=1
                substring_len = mostFreq + rest
                if substring_len>=maxx:
                    maxx=substring_len
            else:
                counter[s[L]]-=1 #Order matters!! This is decremented Since we are moving up and that L is no longer in our counter
                R+=1  #Remember, in sliding window, Right pointer is always incremented.
                L+=1     
        return maxx
        


        
                
            
        
""" My original solution, works but due to Counter being used, time limit exceeded.
 """
def characterReplacement(s: str, k: int) -> int:
    L = 0
    R=0
    maxx = 0
    #if s
    while R<len(s):
        window = s[L:R+1]
        hash = Counter(window)
        mostFreq = max(hash.values())
        #mostFreq = max(hash, key=hash.get)
        rest = len(window)-mostFreq
        if rest<=k:
            R+=1
            if (mostFreq+rest)>maxx:
                maxx=mostFreq + rest
        else:
            L+=1 #dont need to decrement since your counter is being re initialized on every iteration.
            
        
    return maxx




class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1+ countS.get(s[i], 0)
            # the value 0 is the default value for the dictionary
            countT[t[i]] = 1+ countT.get(t[i], 0)
        if countS == countT:
            return True
        else:   
            return False





        
    
    
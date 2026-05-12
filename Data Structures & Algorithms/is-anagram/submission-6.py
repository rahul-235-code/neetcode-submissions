class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_1 = {}
        t_1 = {}

        for i in range(len(s)):
            s_1[s[i]] = 1 + s_1.get(s[i],0)
            t_1[t[i]] = 1 + t_1.get(t[i],0)
        
        return s_1 == t_1
        
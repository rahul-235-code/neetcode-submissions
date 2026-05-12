# class Solution:
#     def isAnagram(self, s: str, t:str) -> bool:
#         if len(s) != len(t):
#             return False
        
#         countS, countT = {},{}

#         for i in range(len(s)):
#             countS[s[i]] = 1 + countS.get(s[i], 0)
#             countT[t[i]] = 1 + countT.get(t[i], 0)
        
#         if countS == countT:
#             return True
#         else:
#             return False

#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         group = list()

#         for i in range(len(strs)):
#             for j in range(i+1, len(strs)):
#                 temp = [strs[i]]
#                 if self.isAnagram(strs[i], strs[j]):
#                     temp.append(strs[j])

#             group.append(temp)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        return countS == countT

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = []  # This will hold the final groups of anagrams
        
        for i in range(len(strs)):
            found = False
            for group in groups:
                # Compare with the first element of the current group
                if self.isAnagram(group[0], strs[i]):  # Use 'self.isAnagram' instead of 'isAnagram'
                    group.append(strs[i])
                    found = True
                    break
            if not found:
                groups.append([strs[i]])

        return groups
    
#The error NameError: name 'isAnagram' is not defined occurs because 
#the method isAnagram is being called without the self keyword inside 
#the groupAnagrams method. In Python, when you call a method within 
#the same class, you must use self.method_name instead of just method_name.


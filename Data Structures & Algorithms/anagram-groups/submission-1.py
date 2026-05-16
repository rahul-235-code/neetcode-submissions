class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l_2 = defaultdict(list)
        for s in strs:
            sorted_s = "".join(sorted(s))
            l_2[sorted_s].append(s)
        return list(l_2.values())
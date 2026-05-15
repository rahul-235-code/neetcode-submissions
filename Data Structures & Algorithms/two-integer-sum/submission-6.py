class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        nums_set = {}

        for i, v in enumerate(nums):
            twosum = target - v
            if twosum in nums_set:
               return [nums_set[twosum], i]
            nums_set[v] = i
    

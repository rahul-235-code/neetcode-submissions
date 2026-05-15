class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        original = set()
        complement = set()
        
        for num in nums:
            original.add(num)
            complement.add(target-num)
            # for case when [3,3] and target is 6
            if (target%2==0 and num == target/2 and nums.count(num) == 2):
                return [nums.index(num), nums.index(num, nums.index(num) + 1)]
            else:
                complement.discard(num)
        
        intersect = next(iter(original.intersection(complement)))
        print(intersect)
        # next(iter()) will pick up one element say 2
        # {2,7}
        # {7,2} for target as 9
        return [nums.index(intersect), nums.index(target-intersect)]

        
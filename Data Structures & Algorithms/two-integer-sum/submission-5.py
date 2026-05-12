class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checkSum = {}

        for index, value in enumerate(nums):

            diff = target - value

            if diff in checkSum:
                return [checkSum[diff], index]
            checkSum[value] = index



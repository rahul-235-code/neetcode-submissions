class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countF = {}

        for i in range(len(nums)):
            countF[nums[i]] = 1 + countF.get(nums[i], 0)

        sorted_values = dict(sorted(countF.items(),key=lambda item: item[1], reverse = True))

        #print(sorted_values)

        keys_list = [key for key in list(sorted_values.keys())[:k]]
        return keys_list

        
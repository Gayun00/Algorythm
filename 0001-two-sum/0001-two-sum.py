class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dictionary = {}

        for i in range(len(nums)):
            dictionary[nums[i]] = i

        for x in range(len(nums)):
            needed_number = target - nums[x]
            if needed_number in dictionary and dictionary[needed_number] != x:
                return [x, dictionary[needed_number]]
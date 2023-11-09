class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        
        for idx,num in enumerate(nums):
            if num not in dict:
                dict[num] = idx
            if target-num in dict and idx != dict[target-num]:
                return [idx, dict[target-num]]
            
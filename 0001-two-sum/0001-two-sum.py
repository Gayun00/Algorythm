class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i in range(len(nums)):
            num = nums[i]
            
            if (target - num) not in dict:
                dict[num] = i
            else:
                return sorted([i, dict[target-num]])
            
            
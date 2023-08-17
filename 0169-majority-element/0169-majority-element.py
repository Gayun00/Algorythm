class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict = {}
        maj  = 0
        for _,element in enumerate(nums):
            if element in dict:
                dict[element] = dict[element] + 1
            else:
                dict[element] = 1
            if dict[element] > len(nums) /2:
                return element
        
        
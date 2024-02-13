class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dict = {}
        
        for num in nums:
            if num in dict:
                return num
            dict[num] = True
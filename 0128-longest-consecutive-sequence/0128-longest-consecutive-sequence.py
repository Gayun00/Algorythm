class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dict = {}
        target = 0
        count = 0
        longestCount = 0
        
        for num in nums:
            dict[num] = True
    
        for num in dict:
            if num - 1 not in dict:
                count = 1
                target = num + 1
                
            while target in dict:
                target += 1
                count += 1
            
            longestCount = max(count, longestCount)
        
        return longestCount
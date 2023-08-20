class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dict = {}
        max_length = 0
        
        for num in nums:
            dict[num]= 1
                
        for num in dict:
            target = num + 1
            count = 1
            
            if num - 1 not in dict:
                while target in dict:
                    target += 1
                    count += 1
                
            max_length = max(max_length, count)
        return max_length
        
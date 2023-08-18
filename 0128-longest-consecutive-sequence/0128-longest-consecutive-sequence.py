class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dict = {}
        longest = 0
        
        for num in nums:
            dict[num] = True
            
        for num in dict:
            if num - 1 not in dict:
                cnt = 1
                target = num + 1
            
                while target in dict:
                    target += 1
                    cnt +=1
                
                longest= max(longest, cnt)
        return longest
        
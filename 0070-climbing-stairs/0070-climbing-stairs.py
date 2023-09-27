class Solution:
    def climbStairs(self, n: int) -> int:
        dict = {}
        if n == 1:
            return 1
        if n == 2:
            return 2
        dict[1] = 1
        dict[2] = 2
        
        for i in range(3, n+1):
            dict[i] = dict[i-1] + dict[i-2]
        return dict[n]
            
        
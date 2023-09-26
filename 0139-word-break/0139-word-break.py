from functools import cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @cache
        def dfs(startIdx):
            if startIdx == len(s):
                return True
            for word in wordDict:
                if s[startIdx: startIdx + len(word)] == word:
                    if dfs(startIdx + len(word)):
                        return True
            return False
                    
        return dfs(0)
            
                
                
        
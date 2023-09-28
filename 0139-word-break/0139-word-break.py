from functools import cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @cache
        
        def dfs(startIdx):
            for word in wordDict:
                n = len(word)
                endIdx = startIdx + n
                
                if startIdx == len(s):
                    return True
                
                if s[startIdx:endIdx]  == word:
                    if dfs(endIdx):
                        return True
            return False
                
            
        return dfs(0)

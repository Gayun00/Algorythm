from itertools import permutations

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        array = list(range(1,n+1))
        comb = list(itertools.permutations(array, n))
        return ''.join(list(map(str, comb[k-1])))
import itertools
import re

def solution(user_id, banned_id):
    n = len(banned_id)
    user_comb = itertools.permutations(user_id, n)
    converted_banned = [string.replace('*','.') for string in banned_id]
    answer = []
        
    for comb in user_comb:
        comb_arr = list(comb)
        flag = True
        
        for i in range(n):
            if re.match(converted_banned[i], comb_arr[i]) and len(converted_banned[i]) == len(comb_arr[i]):
                continue
            else:
                flag = False
                break
        
        if flag:
            if sorted(comb_arr) not in answer:
                answer.append(sorted(comb_arr))
                
    return len(answer)
                
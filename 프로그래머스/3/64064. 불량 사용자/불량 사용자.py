import re
import itertools

def solution(user_id, banned_id):
    n = len(banned_id)
    converted_banned_id = [string.replace('*','.') for string in banned_id]
    combined_user_id = itertools.permutations(user_id, n)
    answer = []

    for user_id in combined_user_id:
        user = list(user_id)
        flag = True
        
        for i in range(n):
            if re.match(converted_banned_id[i], user[i]) and len(user[i]) == len(converted_banned_id[i]):
                continue
            else:
                flag = False
                break
                
        if flag:
            if sorted(user) not in answer:
                answer.append(sorted(user))
                
    return len(answer)
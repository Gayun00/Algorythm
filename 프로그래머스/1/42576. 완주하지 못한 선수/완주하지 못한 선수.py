def solution(participant, completion):
    dict = {}
    for com in completion:
        if com not in dict:
            dict[com] = 1
        else:
            dict[com] += 1
            
    for part in participant:
        if part in dict and dict[part] >=1 :
            dict[part] -=1
        else:
            return part

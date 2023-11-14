

def solution(operations):
    que = []
    
    for operation in operations:
        if operation[0] == "I":
            que.append(int(operation[2:]))
        elif operation[0] == "D":
            if len(que) == 0:
                continue
            if operation[2:] == "-1":
                min_value = min(que)
                index = que.index(min_value)
                del que[index]
            elif operation[2:] == "1":
                max_value = max(que)
                index = que.index(max_value)
                del que[index]
    if len(que) == 0:
        return [0,0]
    else:
        return [max(que),min(que)]
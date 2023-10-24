from collections import deque

def solution(queue1, queue2):
    que1 = deque(queue1)
    que2 = deque(queue2)
    sum1 = sum(que1)
    sum2 = sum(que2)
    limit = len(que1) * 3
    count = 0
    
    if sum1 == sum2:
        return 0
    elif (sum1 + sum2) % 2 == 1:
        return -1
    
    while True:
        if sum1 > sum2:
            popped = que1.popleft()
            que2.append(popped) 
            sum1 -= popped
            sum2 += popped
            count += 1
            
        elif sum2 > sum1:
            popped = que2.popleft()
            que1.append(popped)
            sum1 += popped
            sum2 -= popped
            count += 1
            
        else:
            break
        if limit == count:
            return -1

    return count
        
    



def solution(stones, k):
    right = max(stones)
    left = min(stones)
    answer = 0
    
    while left <= right:
        mid = int((right + left) / 2)
        emptyStones = 0
        
        for stone in stones:
            if stone <= mid:
                emptyStones += 1
            else:
                emptyStones = 0
                
            if emptyStones == k:
                break
                
        if emptyStones < k:
            left = mid + 1
        else:
            right = mid - 1
            answer = mid

    return answer
    
    
        
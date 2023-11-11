def solution(stones, k):
    answer = 0
    left = 1
    right = max(stones)
    
    while left <= right:
        mid = (left + right)//2
        emptyStones = 0
        
        for stone in stones:
            if stone - mid <= 0:
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
def solution(stones, k):
    right = max(stones)
    left = min(stones)
    answer = 0
    
    while left <= right:
        mid = int((left + right)/2)
        empty_count = 0
        
        for stone in stones:
            if stone - mid <= 0:
                empty_count += 1
            else:
                empty_count = 0
                
            if empty_count == k:
                break
        
        if empty_count >= k:
            right = mid - 1
            answer = mid
        else:
            left = mid + 1
            
    return answer
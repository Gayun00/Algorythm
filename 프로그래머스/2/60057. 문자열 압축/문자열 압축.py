def solution(s):
    result = []
    
    for i in range(1, len(s)+1):
        b = ''
        count = 1
        temp = s[:i]
        
        for j in range(i, len(s) + i, i):
            if temp == s[j:i+j]:
                count += 1
                
            else:
                if count != 1:
                    b = b + str(count) + temp
                else:
                    b = b + temp
                temp = s[j:i+j]
                count = 1
                
        result.append(len(b))
    return min(result)
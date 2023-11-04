def solution(cap, n, deliveries, pickups):  
    idps = [(i,d,p) for i,(d,p) in enumerate(zip(deliveries, pickups),1) if d or p]
    delivery = 0
    pickup = 0
    answer = 0
    
    while idps:
        i,d,p = idps.pop()
        delivery += d
        pickup += p
        
#       배달, 수거 하나라도 있다면 들러야 하니 양수인지 확인
        while delivery > 0 or pickup > 0:
#           둘다 0이 되도록 이동
#           이동하면서 cap만큼 배달,수거 가능하므로 각각 빼주기
            delivery -= cap
            pickup -= cap
#         왕복 거리이므로 2 곱하기
            answer += 2 * i
    return answer
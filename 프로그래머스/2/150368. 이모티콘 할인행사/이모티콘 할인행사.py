from itertools import product

def solution(users, emoticons):
    discount_rates = [10, 20, 30, 40]
    comb_discounts = list(product(discount_rates, repeat = len(emoticons)))
    result = []
    
    for comb_discount in comb_discounts:
        members = 0
        income = 0
        
        for required_discount, budget in users:
            purchased = 0
            
            for i in range(len(emoticons)):
                if comb_discount[i] >= required_discount:
                    price = emoticons[i] - emoticons[i] * comb_discount[i] * 0.01
                    purchased += int(price)
            if purchased >= budget:
                members += 1
            else:
                income += purchased
        result.append((members, income))
        
    answer = sorted(result, reverse=True, key=lambda x: (x[0], x[1]))

    return answer[0]
        
    

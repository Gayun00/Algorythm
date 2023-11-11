from itertools import product

def solution(users, emoticons):
    discount_rates = [10, 20, 30, 40]
    combined_discounts = list(product(discount_rates, repeat=len(emoticons)))
    result = []
    
    for discounts in combined_discounts:
        members = 0
        income = 0
        
        for user_discount, user_price in users:
            purchased = 0
            
            for i in range(len(emoticons)):
                if user_discount <= discounts[i]:
                    price = emoticons[i] - emoticons[i] * discounts[i] * 0.01
                    purchased += price
                    
            if purchased >= user_price:
                members +=1
            else:
                income += purchased

        result.append((members, income))
    answer = sorted(result, reverse=True, key=lambda x:(x[0], x[1]))
    
    return answer[0]
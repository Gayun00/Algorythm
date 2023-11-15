import collections
import itertools

def solution(orders, course):
    answer = []
    
    for course_size in course:
        order_combinations = []
        
        for order in orders:
            order_combinations += itertools.combinations(sorted(order), course_size)
        
        most_ordered = collections.Counter(order_combinations).most_common()
        
        for comb, count in most_ordered:
            if count > 1 and count == most_ordered[0][1]:
                answer.append(comb)
    
    return ["".join(count) for count in sorted(answer)]

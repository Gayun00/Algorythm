import itertools
import re

def solution(expression):
    combinations = list(itertools.permutations(["+","-","*"],3))
    splited = re.split("([-+*]{1})", expression)
    results = []

    for combination in combinations:
        comb = list(combination)
        new_expression = splited[:]
        
        for sign in comb:
            while sign in new_expression:
                index = new_expression.index(sign)
                result = str(eval(new_expression[index-1] + sign + new_expression[index+1]))
                del new_expression[index:index+2]
                new_expression[index-1] = result
                
        results.append(abs(int(new_expression[0])))
        
    return max(results)
        
                
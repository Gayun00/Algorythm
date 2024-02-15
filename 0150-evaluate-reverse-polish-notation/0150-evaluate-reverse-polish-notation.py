import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ['+', '-', '*', '/']
        
        def calcaulate(tokens):
            if len(tokens) == 1:
                return int(tokens[0])

            for i, token in enumerate(tokens[:]):
                if token in operators:
                    result = 0
                    if token == "/" and (int(tokens[i-2]) < 0 or int(tokens[i-1]) < 0):
                        result = str(int(int(tokens[i-2]) / int(tokens[i-1])))
                        print(result)
                    else:
                        result = str(math.floor(eval(tokens[i-2] + token + tokens[i-1])))
                    tokens[i] = result
                    del tokens[i-2:i]
                    return calcaulate(tokens)

        return calcaulate(tokens)
        
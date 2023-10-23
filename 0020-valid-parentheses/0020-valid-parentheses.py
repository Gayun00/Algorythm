class Solution:
    def isValid(self, s: str) -> bool:
        dict = {
            "{":"}",
            "[":"]",
            "(":")"
        }
        stack = []
        
        for curr in s:
            if not len(stack):
                if curr not in dict:
                    return False
                stack.append(curr)
            else:
                last_stack_el = stack[-1]
                if last_stack_el in dict:
                    if dict[last_stack_el] == curr:
                      stack.pop()
                    else:
                      stack.append(curr)
        
        return not bool(stack)
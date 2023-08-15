class Solution:
    def isValid(self, s: str) -> bool:
      strArray = list(s)
      stack = []

      pairs = {
        '(': ")",
        "{": "}",
        "[": "]"
      }

      for cur_str in strArray :

        if not stack:
          if not cur_str in pairs:
            return False
          stack.append(cur_str)
        else:
          last_stack_el = stack[-1]
          if last_stack_el in pairs:
            if pairs[last_stack_el] == cur_str:
              stack.pop()
            else:
              stack.append(cur_str)

      return not bool(stack)
        
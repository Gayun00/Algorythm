def solution(board, moves):
    stack = []
    answer = 0
    
    for move in moves:
        for row in range(len(board)):
            cur = board[row][move - 1]
            if cur:
                if len(stack) > 0 and stack[-1] == cur:
                    stack.pop()
                    answer += 2
                else:
                    stack.append(cur)
                board[row][move - 1] = 0
                break 
    return answer
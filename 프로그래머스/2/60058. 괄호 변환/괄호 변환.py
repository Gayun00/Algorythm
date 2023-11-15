from collections import deque


def separate_u_v(p):
    open_p, close_p = 0, 0
    for i in range(len(p)):
        if p[i] == "(":
            open_p += 1
        else:
            close_p += 1
        if open_p == close_p:
            return p[: i + 1], p[i + 1 :]


def check_balance(u):
    stack = deque()
    for i in u:
        if i == "(":
            stack.append(i)
        else:
            if not stack:
                return False
            stack.pop()
    return True if not stack else False


def solution(p):
    if not p:
        return p

    u, v = separate_u_v(p)

    if check_balance(u):
        return u + solution(v)
    else:
        answer = "("
        answer += solution(v)
        answer += ")"

        for pp in u[1 : len(u) - 1]:
            if pp == "(":
                answer += ")"
            else:
                answer += "("
    return answer

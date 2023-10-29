class Node:
    def __init__(self):
        self.prev = None
        self.next = None
        self.removed = False


def solution(n, k, cmd):
    deleted = []
    nodes = [Node() for _ in range(n)]

    for i in range(1, n):
        nodes[i - 1].next = nodes[i]
        nodes[i].prev = nodes[i - 1]

    cur = nodes[k]

    for command in cmd:
        if command[0] == "U":
            x = int(command[2:])
            for i in range(x):
                cur = cur.prev
        elif command[0] == "D":
            x = int(command[2:])
            for i in range(x):
                cur = cur.next
        elif command[0] == "C":
            cur.removed = True
            deleted.append(cur)
            up = cur.prev
            down = cur.next

            if up:
                up.next = down
            if down:
                down.prev = up
                cur = down
            else:
                cur = up
        else:
            deletedNode = deleted.pop()
            deletedNode.removed = False
            up = deletedNode.prev
            down = deletedNode.next

            if up:
                up.next = deletedNode
            if down:
                down.prev = deletedNode

    answer = ""
    for i in range(n):
        if nodes[i].removed:
            answer += "X"
        else:
            answer += "O"
    return answer

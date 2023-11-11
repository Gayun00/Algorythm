import sys

class Node:
    def __init__(self, id, x, y):
        self.left = None
        self.right= None
        self.id = id
        self.x = x
        self.y = y
        
    def __lt__(self, other):
        if self.y == other.y:
            return self.x < other.x
        return self.y > other.y
            
    
def linkNode(parent, child):
    if child.x < parent.x:
        if parent.left is None:
            parent.left = child
        else:
            linkNode(parent.left, child)
    else:
        if parent.right is None:
            parent.right = child
        else:
            linkNode(parent.right, child)

def preorder(ans, node):
    if node is None:
        return
    ans.append(node.id)
    preorder(ans, node.left)
    preorder(ans, node.right)
    
def postorder(ans, node):
    if node is None:
        return
    postorder(ans, node.left)
    postorder(ans, node.right)
    ans.append(node.id)
    

def solution(nodeinfo):
    sys.setrecursionlimit(1500)
    node_list = []
    
    for i in range(len(nodeinfo)):
        node_list.append(Node(i+1, nodeinfo[i][0], nodeinfo[i][1]))
        
    node_list.sort()
    
    root = node_list[0]
    
    for i in range(1, len(nodeinfo)):
        linkNode(root, node_list[i])
        
    answer = [[], []]
    
    preorder(answer[0], root)
    postorder(answer[1], root)
    
    return answer
    
        
    
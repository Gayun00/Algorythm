from typing import List,Dict
from collections import defaultdict

SHEEP = 0
WOOLF = 1

def solution(info, edges):
    parent2children = build_parent2children(edges)
    return max_sheep([0], parent2children, info,0,0)

def build_parent2children(edges) -> Dict[int, List[int]]:
    parent2children = defaultdict(list)
    for parent, child in edges:
        parent2children[parent].append(child)
    return parent2children

def max_sheep(nodes, parent2children, info, s, w):
    if not nodes:
        return s
    max_s = s
    
    for idx, node in enumerate(nodes):
        if info[node] == SHEEP:
            max_s = max(max_sheep(nodes[:idx] + nodes[idx+1:] + parent2children[node], parent2children, info, s+1, w), max_s)
        elif s > w+1:
            max_s = max(max_sheep(nodes[:idx] + nodes[idx+1:] + parent2children[node], parent2children, info, s, w+1), max_s)
    return max_s
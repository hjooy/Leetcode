"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None
        map = {}

        def dfs(node: Optional['Node']) -> 'Node':
            if node in map:
                return map[node]

            new_node = Node(node.val)
            map[node] = new_node
            for n in node.neighbors:
                new_node.neighbors.append(dfs(n))

            return new_node

        return dfs(node)
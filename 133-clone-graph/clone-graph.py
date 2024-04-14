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
        q = deque([node])

        while q:
            cur = q.popleft()
            if map.get(cur) is None:
                map[cur] = Node(cur.val)
            
            for nei in cur.neighbors:
                if map.get(nei) is None:
                    map[nei] = Node(nei.val)
                    q.append(nei)
                    
                map[nei].neighbors.append(map.get(cur))

        return map.get(node)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:  
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        result = 0
        def dfs(cur: TreeNode, sum: int) -> int:
            if not cur: return 0
            sum += cur.val
            dfs(cur.left, sum << 1)
            dfs(cur.right, sum << 1)
            if not cur.left and not cur.right:
                nonlocal result
                result += sum
            
        dfs(root, 0)
        return result


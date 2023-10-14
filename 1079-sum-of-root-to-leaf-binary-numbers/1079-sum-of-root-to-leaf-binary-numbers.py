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
            if not cur: return
            sum += cur.val
            dfs(cur.left, sum * 2)
            dfs(cur.right, sum * 2)
            if not cur.left and not cur.right:
                nonlocal result
                result += sum
            #sum /= 2
            #sum -= cur.val

        dfs(root, 0)
        return result


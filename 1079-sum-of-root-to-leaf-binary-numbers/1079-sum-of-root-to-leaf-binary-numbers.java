/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    int result = 0;
    public int sumRootToLeaf(TreeNode root) {
        dfs(root, 0);
        return result;
    }

    private void dfs(TreeNode cur, int sum) {
        if (cur == null) return;
        sum += cur.val;
        if(cur.left == null && cur.right == null) {
            result += sum;
        }
        dfs(cur.left, sum * 2);
        dfs(cur.right, sum * 2);
        sum -= cur.val;
        sum /= 2;
    }
}
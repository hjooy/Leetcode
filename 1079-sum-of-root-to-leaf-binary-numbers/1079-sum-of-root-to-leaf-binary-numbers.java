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
        StringBuilder str = new StringBuilder();
        dfs(root, str);
        return result;
    }

    private void dfs(TreeNode cur, StringBuilder str) {
        if (cur == null) return;
        str.append(cur.val);
        dfs(cur.left, str);
        dfs(cur.right, str);
        if(cur.left == null && cur.right == null) {
            int pow = 1;
            for (int i = str.length() - 1; i >= 0 ; i--) {
                result += (str.charAt(i) - '0') * pow;
                pow *= 2;
            }
        } 
        str.deleteCharAt(str.length() - 1);
    }
}
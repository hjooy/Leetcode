class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        Stack<Integer> s = new Stack<>();
        dfs(nums, 0, s, result);

        return result;
    }

    public void dfs(int[] nums, int i, Stack<Integer> s, List<List<Integer>> result) {
        if (i == nums.length) {
            result.add(new ArrayList(s));
            return;
        }
        s.push(nums[i]);
        dfs(nums, i + 1, s, result);
        s.pop();
        dfs(nums, i + 1, s, result);
    }
}
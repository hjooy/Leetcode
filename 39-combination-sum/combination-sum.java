class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> result = new ArrayList<>();
        Stack<Integer> s = new Stack<>();
        helper(candidates, 0, 0, target, s, result);
        return result;
    }

    public void helper(int[] candidates, int i, int sum, int target, Stack<Integer> com, List<List<Integer>> result) {
        if (sum > target) return;
        else if (sum == target) {
            result.add(new ArrayList(com));
            return;
        }
        sum += candidates[i];
        com.push(candidates[i]);
        helper(candidates, i, sum, target, com, result);
        sum -= candidates[i];
        com.pop();
        if (i < candidates.length - 1) {
            helper(candidates, i + 1, sum, target, com, result);
        }
    }
}
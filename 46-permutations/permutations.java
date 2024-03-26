class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        List<Integer> cur = new ArrayList<>();
        backtrack(nums, cur, result);
        return result;
    }

    private void backtrack(int[] nums, List<Integer> cur, List<List<Integer>> result) {
        if (cur.size() == nums.length) {
            result.add(new ArrayList<>(cur));
            return;
        }
        for (int n : nums) {
            if (cur.contains(n)) continue;
            cur.add(n);
            backtrack(nums, cur, result);
            cur.remove(cur.size() - 1);
        }
    }
}
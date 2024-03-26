class Solution {
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        Set<List<Integer>> result = new HashSet<>();
        backtrack(0, new ArrayList<>(), nums, result);
        return List.copyOf(result);
        //return new ArrayList<>(result);
    }

    private void backtrack(int idx, List<Integer> cur, int[] nums, Set<List<Integer>> result) {
        if (idx == nums.length) {
            List<Integer> tmp = new ArrayList<>(cur);
            tmp.sort(Comparator.naturalOrder());
            result.add(tmp);
            return;
        }
        
        cur.add(nums[idx]);
        backtrack(idx + 1, cur, nums, result);
        cur.remove(cur.size() - 1);
        backtrack(idx + 1, cur, nums, result);
    }
}
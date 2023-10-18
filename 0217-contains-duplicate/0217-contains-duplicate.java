class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> set = new HashSet<>();
        int tmp = 0;
        for (int i = 0; i < nums.length; i++) {
            tmp = nums[i];
            if (set.contains(tmp)) {
                return true;
            }
            set.add(tmp);
        }
        return false;
    }
}
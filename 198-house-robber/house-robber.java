class Solution {
    public int rob(int[] nums) {
        int n = nums.length;
        if (n == 1) return nums[0];
        else if (n == 2) return nums[0] > nums[1] ? nums[0] : nums[1];
        
        int dp1 = nums[0];
        int dp2 = nums[0] > nums[1] ? nums[0] : nums[1];

        for (int i = 2; i < n; i++) {
            int tmp = dp2;
            dp2 = dp1 + nums[i] > dp2 ? dp1 + nums[i] : dp2;
            dp1 = tmp;
        }

        return dp1 > dp2 ? dp1 : dp2;
    }
}
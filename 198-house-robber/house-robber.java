class Solution {
    public int rob(int[] nums) {
        int n = nums.length;
        int ans = 0;
        int[] dp = new int[n];

        for (int i = 0; i < n; i++) {
            if (i < 2) dp[i] = nums[i];
            else if (i < 3) dp[i] = nums[i] + dp[i - 2];
            else dp[i] = (dp[i - 2] > dp[i - 3] ? dp[i - 2] : dp[i - 3]) + nums[i];
        }

        for (int i : dp) {
            if (i > ans) ans = i;
        }

        return ans;
    }
}
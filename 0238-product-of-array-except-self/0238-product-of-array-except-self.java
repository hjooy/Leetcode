class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] ans = new int[n];
        for (int i = 0; i < n; i++) {
            ans[i] = 1;
        }

        int accumulated_product = 1;
        for (int i = 0; i < n - 1; i++) {
            accumulated_product *= nums[i];
            ans[i + 1] *= accumulated_product;
        }
        
        accumulated_product = 1;
        for (int i = n - 1; i > 0; i--) {
            accumulated_product *= nums[i];
            ans[i - 1] *= accumulated_product;
        }

        return ans;
    }
}
class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] ans = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            ans[i] = 1;
        }

        int accumulated_product = 1;
        for (int i = 0; i < nums.length - 1; i++) {
            accumulated_product *= nums[i];
            ans[i + 1] *= accumulated_product;
        }
        
        accumulated_product = 1;
        for (int i = nums.length - 1; i > 0; i--) {
            accumulated_product *= nums[i];
            ans[i - 1] *= accumulated_product;
        }

        return ans;
    }
}
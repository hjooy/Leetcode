class Solution {
    public int sumOfUnique(int[] nums) {
        int[] count = new int[101];
        int sum = 0;

        for (int num : nums) {
            if (count[num] == 0) {
                count[num] = 1;
            }
            else if (count[num] == 1) {
                count[num] = -1;
            }
        }

        for (int i = 0; i < 101; i++) {
            if (count[i] == 1) {
                sum += i;
            }
        }
        return sum;
    }
}
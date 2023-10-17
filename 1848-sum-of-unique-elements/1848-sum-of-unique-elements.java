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

        for (int num : nums) {
            if (count[num] == 1) {
                sum += num;
            }
        }
        return sum;
    }
}
class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> numSet = new HashSet<>();

        for (int n : nums) { numSet.add(n); }

        int max = 0;
        int length;
        for (int n : nums) {
            if (!numSet.contains(n - 1)) {
                length = 0;
                while (numSet.contains(n)) {
                    length++;
                    n++;
                }
                max = (max < length) ? length : max;
            }
        }

        return max;
    }
}
class Solution {
    public int longestConsecutive(int[] nums) {
        Map<Integer, Integer> lengthMap = new HashMap<>();
        
        int max = 0;
        for (int n : nums) {
            if (!lengthMap.containsKey(n)) {
                int left = (lengthMap.containsKey(n - 1)) ? lengthMap.get(n - 1) : 0;
                int right = (lengthMap.containsKey(n + 1)) ? lengthMap.get(n + 1) : 0;
                int length = left + right + 1;
                lengthMap.put(n, length);
                lengthMap.put(n - left, length);
                lengthMap.put(n + right, length);
                max = (max < length) ? length : max;
            }
        }

        return max;
    }
}
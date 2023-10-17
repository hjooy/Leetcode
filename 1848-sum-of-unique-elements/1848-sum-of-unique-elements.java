class Solution {
    public int sumOfUnique(int[] nums) {
        Map<Integer, Integer> map = new HashMap<>();
        Set<Integer> keySet;
        int ans = 0;
        int tmp = 0;

        for (int i = 0; i < nums.length; i++) {
            if (!map.containsKey(nums[i])) {
                map.put(nums[i], 1);
            }
            else {
                tmp = map.get(nums[i]);
                map.replace(nums[i], tmp + 1);
            }
        }

        keySet = map.keySet();
        for (Integer i : keySet) {
            if (map.get(i) == 1){
                ans += i;
            }
        }

        return ans;
    }
}
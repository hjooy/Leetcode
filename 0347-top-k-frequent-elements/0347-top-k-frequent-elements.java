class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<>();

        for (int n : nums) {
            map.put(n, map.getOrDefault(n, 0) + 1);
        }

        Map<Integer, List<Integer>> freqMap = new TreeMap<>();
        for (int key : map.keySet()) {
            int cnt = -map.get(key);
            if (freqMap.get(cnt) == null) {
                freqMap.put(cnt, new LinkedList<Integer>());
            }
            freqMap.get(cnt).add(key);
        }

        int[] ans = new int[k];
        for (int key : freqMap.keySet()) {
            for (int n : freqMap.get(key)) {
                if (k == 0) break;
                ans[k-1] = n;
                k--;
            }
        }

        return ans;
    }
}
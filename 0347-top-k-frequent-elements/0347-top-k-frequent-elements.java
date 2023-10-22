class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<>();

        for (int n : nums) {
            map.put(n, map.getOrDefault(n, 0) + 1);
        }

        List<Integer>[] bucket = new List[nums.length + 1];
        for (int key : map.keySet()) {
            int cnt = map.get(key);
            if (bucket[cnt] == null) {
                bucket[cnt] = new LinkedList<Integer>();
            }
            bucket[cnt].add(key);
        }

        int[] ans = new int[k];
        for (int i = bucket.length - 1; i >= 0; i--) {
            if (bucket[i] == null) continue;
            for (int num : bucket[i]) {
                if (k == 0) break;
                ans[k-1] = num;
                k--;
            }
        }

        return ans;
    }
}
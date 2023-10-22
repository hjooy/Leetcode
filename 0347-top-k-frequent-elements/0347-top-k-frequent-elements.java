class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<>();

        for (int n : nums) {
            map.put(n, map.getOrDefault(n, 0) + 1);
        }

        PriorityQueue<Integer> maxHeap = new PriorityQueue<>((a, b)->map.get(b) - map.get(a));
        for (int key : map.keySet()) {
            maxHeap.add(key);
        }

        int[] ans = new int[k];
        while (k > 0) {
            ans[k-1] = maxHeap.poll();
            k--;
        }

        return ans;
    }
}
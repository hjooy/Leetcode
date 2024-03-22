class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<List<Integer>>> dp = new ArrayList<>();
        for (int i = 0; i <= target; i++) {
            dp.add(new ArrayList<>());
        }

        for (int c : candidates) {
            for (int i = c; i <= target; i++) {
                if (i == c) dp.get(i).add(Arrays.asList(c));
                else if (i > c) {
                    for (List<Integer> comb : dp.get(i - c)) {
                        List<Integer> tmp = new ArrayList<>();
                        tmp.addAll(comb);
                        tmp.add(c);
                        dp.get(i).add(tmp);
                    }
                }
            }
        }
        return dp.get(target);
    }
}
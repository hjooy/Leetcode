class Solution {
    public boolean isAnagram(String s, String t) {
        Map<Integer, Integer> dict = new HashMap<>();
        int tmp = 0;
        for (int i = 0; i < s.length(); i++) {
            tmp = s.charAt(i) - '0';
            if (dict.containsKey(tmp)) {
                dict.replace(tmp, dict.get(tmp) + 1);
            }
            else {
                dict.put(tmp, 1); 
            }
        }
        for (int i = 0; i < t.length(); i++) {
            tmp = t.charAt(i) - '0';
            if (dict.containsKey(tmp)) {
                dict.replace(tmp, dict.get(tmp) - 1);
            }
            else {
                dict.put(tmp, -1); 
            }
        }
        for (Integer key : dict.keySet()) {
            if (dict.get(key) != 0) return false;
        }
        return true;
    }
}
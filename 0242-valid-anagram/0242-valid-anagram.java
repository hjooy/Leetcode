class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;
        Map<Character, Integer> dict = new HashMap<>();
        for (char c : s.toCharArray()) {
            dict.put(c, dict.getOrDefault(c, 0) + 1);
        }
        for (char c : t.toCharArray()) {
            dict.put(c, dict.getOrDefault(c, 0) - 1);
        }
        for (int x : dict.values()) {
            if (x != 0) return false;
        }
        return true;
    }
}
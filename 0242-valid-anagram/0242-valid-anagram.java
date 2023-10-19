class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;
        int[] arr = new int[26];
        int tmp = 0;
        for (int i = 0; i < s.length(); i++) {
            tmp = s.charAt(i) - 'a';
            arr[tmp] += 1;
            tmp = t.charAt(i) - 'a';
            arr[tmp] -= 1;
        }
        for (int i = 0; i < 26; i++) {
            if (arr[i] != 0) return false;
        }
        return true;
    }
}
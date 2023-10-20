class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> ans = new ArrayList<>();
        Map<String, List<String>> map = new HashMap<>();
        String sortedStr;
        char[] charArr;
        List<String> tmp;

        for (String str : strs) {
            charArr = str.toCharArray();
            Arrays.sort(charArr);
            sortedStr = new String(charArr);

            if (map.containsKey(sortedStr)) {
                tmp = map.get(sortedStr);
                tmp.add(str);
                map.put(sortedStr, tmp);
            }
            else {
                tmp = new ArrayList<String>();
                tmp.add(str);
                map.put(sortedStr, tmp);
            }
        }

        for (String key : map.keySet()) {
            ans.add(map.get(key));
        }
        
        return ans;
    }
}
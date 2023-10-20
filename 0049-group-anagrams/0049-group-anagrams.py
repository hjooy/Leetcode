class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        dict = {}
        for str in strs:
            tmp = ''.join(sorted(str))
            if tmp in dict:
                dict[tmp].append(str)
            else:
                dict[tmp] = [str]

        for key in dict:
            ans.append(dict[key])
        
        return ans
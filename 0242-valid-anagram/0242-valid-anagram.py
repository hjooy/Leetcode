class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict = {}
        for c in s:
            if c in dict.keys():
                dict[c] += 1
            else: dict[c] = 1
        for c in t:
            if c in dict.keys():
                dict[c] -= 1
            else: dict[c] = -1
        for key in dict.keys():
            if dict[key] is not 0:
                return False
        return True
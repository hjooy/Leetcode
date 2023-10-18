class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list = [0] * 26
        for c in s:
            list[ord(c) - 97] += 1
        for c in t:
            list[ord(c) - 97] -= 1
        for x in list:
            if x is not 0:
                return False
        return True
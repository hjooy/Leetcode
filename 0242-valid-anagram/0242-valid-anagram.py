class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
            if len(s) != len(t): return False
            for c in set(s):
                if s.count(c) != t.count(c):
                    return False
            return True

# Time complexity: O(n^2)
#               - len(): O(1) / set(): O(n) / str.count(): O(n)
# Space complexity: O(n)
#               - set(n): O(n)
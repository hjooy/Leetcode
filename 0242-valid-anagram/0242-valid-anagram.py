class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
            if len(s) != len(t): return False
            return sorted(s) == sorted(t)

# Time complexity: O(n log n)
#               - len(): O(1) / sorted(): O(n log n)
# Space complexity: O(n)
#               - sorted() returns a sorted list: O(n)
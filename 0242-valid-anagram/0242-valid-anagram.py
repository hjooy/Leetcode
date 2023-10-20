class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
            dict = defaultdict(int)
            for c in s:
                dict[c] += 1
            for c in t:
                dict[c] -= 1
            for v in dict.values():
                if v is not 0: return False
            return True

# Time complexity: O(n)
# Space complexity: O(n)

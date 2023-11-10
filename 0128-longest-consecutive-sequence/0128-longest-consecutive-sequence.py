class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        best = 0
        dict = {}
        for n in nums:
            if n not in dict:
                left = 0 if n - 1 not in dict else dict[n - 1]
                right = 0 if n + 1 not in dict else dict[n + 1]
                length = left + right + 1
                dict[n] = length
                dict[n - left] = length
                dict[n + right] = length
                best = max(best, length)
        return best
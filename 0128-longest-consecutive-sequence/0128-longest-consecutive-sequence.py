class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        best = 0
        num_set = set(nums)
        for n in nums:
            if n - 1 not in num_set:
                length = 1
                while n + length in num_set:
                    length += 1
                if best < length: best = length
        return best
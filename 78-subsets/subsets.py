class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def helper(nums: List[int], i: int, s: List[int]):
            if i == len(nums):
                result.add(tuple(s))
                return
            t = s[:]
            t.append(nums[i])
            helper(nums, i + 1, t)
            t.remove(nums[i])
            helper(nums, i + 1, t)

        result = set()
        helper(nums, 0, [])
        return result
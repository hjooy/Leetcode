class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        appeared = set(nums)
        return len(appeared) != len(nums)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        
        for i, num in enumerate(nums):
            if target - num in dict:
                return [i, dict[target - num]]
            dict[num] = i

        return []

# Time complexity: O(n)
# Space complexity: O(n)
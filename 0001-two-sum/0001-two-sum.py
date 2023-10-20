class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                # should not use is operator to compare integers!
                if nums[i] + nums[j] == target: 
                    ans = [i, j]
        return ans

# Time complexity: O(n^2)
# Space complexity: O(1)
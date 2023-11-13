class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        nums_set = set(nums)
        nums.sort()

        for i, n in enumerate(nums):
            if i == len(nums) - 2:
                break
            j = i + 1
            k = len(nums) - 1
            while j < k:
                sum = nums[j] + nums[k]
                if sum > -n:
                    k -= 1
                elif sum < -n:
                    j += 1
                else:
                    result.add(tuple(sorted([n, nums[j], nums[k]])))
                    k -= 1
                           
        return [list(i) for i in result]
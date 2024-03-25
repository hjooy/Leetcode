class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []
        def dfs(cur: List[int], used: List[int]):
            if used.count(1) == len(used):
                output.append(cur)
                return;
            for i, n in enumerate(nums):
                if used[i] != 1:
                    new_used = used[:]
                    new_used[i] = 1
                    dfs(cur + [nums[i]], new_used)
            
        dfs([], [0] * (len(nums)))

        return output
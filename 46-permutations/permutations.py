class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []
        def dfs(cur: List[int]):
            if len(cur) == len(nums):
                output.append(cur)
                return;
            for i, n in enumerate(nums):
                if n in cur: continue
                dfs(cur + [n])

        dfs([])

        return output
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []
        def backtrack(cur: List[int]):
            if len(cur) == len(nums):
                output.append(cur[:])
                return;
            for i, n in enumerate(nums):
                if n in cur: continue
                cur.append(n)
                backtrack(cur)
                cur.pop()

        backtrack([])

        return output
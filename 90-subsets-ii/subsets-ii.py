class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = set()

        def dfs(idx: int, cur: List[int], result: Set[Tuple[int]]):
            if idx == len(nums):
                result.add(tuple(sorted(cur)))
                return
            cur.append(nums[idx])
            dfs(idx + 1, cur, result)
            cur.pop(-1)
            dfs(idx + 1, cur, result)

        dfs(0, [], result)
        return list(result)
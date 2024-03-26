class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        vec = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(r:int, c:int, cur:List[int], max:List[int]):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == 0:
                max[0] = cur[0] if max[0] < cur[0] else max[0]
                return
            grid[r][c] = 0
            cur[0] += 1
            for v in vec:
                next_r = r + v[0]
                next_c = c + v[1]
                dfs(next_r, next_c, cur, max)

        max = [0]
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                cur = [0]
                dfs(r, c, cur, max)
        
        return max[0]
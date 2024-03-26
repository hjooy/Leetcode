class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(r:int, c:int) -> int:
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == 0:    
                return 0
            grid[r][c] = 0
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

        ans = 0
        for r in range(len(grid)): 
            for c in range(len(grid[0])): 
                if grid[r][c] == 1:
                    ans = max(ans, dfs(r, c)
                    )
        return ans
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        result = []
        m = len(heights)
        n = len(heights[0])

        flows_to_p = [[False for _ in range(n)] for _ in range(m)]
        flows_to_a = [[False for _ in range(n)] for _ in range(m)]

        def dfs(cur_r: int, cur_c: int, prev_height: int, flows: List[List[bool]]):
            if cur_r < 0 or cur_r >= m or cur_c < 0 or cur_c >= n or prev_height > heights[cur_r][cur_c] or flows[cur_r][cur_c]:
                return
            flows[cur_r][cur_c] = True
            dfs(cur_r - 1, cur_c, heights[cur_r][cur_c], flows)
            dfs(cur_r + 1, cur_c, heights[cur_r][cur_c], flows)
            dfs(cur_r, cur_c - 1, heights[cur_r][cur_c], flows)
            dfs(cur_r, cur_c + 1, heights[cur_r][cur_c], flows)
        
        for r in range(m):
            dfs(r, 0, heights[r][0], flows_to_p)
            dfs(r, n - 1, heights[r][n - 1], flows_to_a)
        
        for c in range(n):
            dfs(0, c, heights[0][c], flows_to_p)
            dfs(m - 1, c, heights[m - 1][c], flows_to_a)
        
        for r in range(m):
            for c in range(n):
                if flows_to_p[r][c] and flows_to_a[r][c]:
                    result.append([r, c])
        
        return result
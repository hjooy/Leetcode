class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        vec_r = [0, 0, -1, 1]
        vec_c = [-1, 1, 0, 0]
        visited = [ [0] * (len(grid[0])) for _ in range(len(grid)) ]

        def dfs(r: int, c: int):
            if visited[r][c] == 1 or grid[r][c] == "0":
                return;
            visited[r][c] = 1
            for i in range(4):
                new_r = r + vec_r[i]
                new_c = c + vec_c[i]
                if new_r >= 0 and new_r < len(grid) and new_c >=0 and new_c < len(grid[0]):
                    if visited[new_r][new_c] == 0 and grid[new_r][new_c] == "1":
                        dfs(new_r, new_c) 
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if visited[i][j] == 1 or grid[i][j] == "0":
                    continue
                dfs(i, j)
                count += 1

        return count
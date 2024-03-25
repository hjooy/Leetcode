class Solution {
    int[][] visited;
    int[] vec_r = new int[]{0, 0, -1, 1};
    int[] vec_c = new int[]{-1, 1, 0, 0};
    int count = 0;

    public int numIslands(char[][] grid) {
        visited = new int[grid.length][grid[0].length];

        for (int r = 0; r < grid.length; r++) {
            for (int c = 0; c < grid[0].length; c++) {
                if (visited[r][c] == 1 || grid[r][c] == '0') continue;
                dfs(r, c, grid);
                count += 1;
            } 
        }

        return count;
    }

    private void dfs(int r, int c, char[][] grid) {
        if (visited[r][c] == 1 || grid[r][c] == '0') return;
        visited[r][c] = 1;
        for (int i = 0; i < 4; i++) {
            int new_r = r + vec_r[i];
            int new_c = c + vec_c[i];
            if (new_r < 0 || new_r >= grid.length || new_c < 0 || new_c >= grid[0].length) continue;
            if (visited[new_r][new_c] == 1 || grid[new_r][new_c] == '0') continue;
            dfs(new_r, new_c, grid);
        }
    }
}
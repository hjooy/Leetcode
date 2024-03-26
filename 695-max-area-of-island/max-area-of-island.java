class Solution {
    int[] vec_r = {0, 0, -1, 1};
    int[] vec_c = {1, -1, 0, 0};

    public int maxAreaOfIsland(int[][] grid) {
        int[] maxSize = {0};
        int[] tmpSize;
        for (int r = 0; r < grid.length; r++) {
            for (int c = 0; c < grid[0].length; c++) {
                if (grid[r][c] == 0) continue;
                tmpSize = new int[]{0};
                dfs(grid, r, c, maxSize, tmpSize);
            }
        }
            
        return maxSize[0];
    }

    private void dfs(int[][] grid, int r, int c, int[] maxSize, int[] curSize) {
        if (r < 0 || r >= grid.length || c < 0 || c >= grid[0].length || grid[r][c] == 0) {
            if (maxSize[0] < curSize[0]) maxSize[0] = curSize[0];
            return;
        }
        curSize[0] += 1;
        grid[r][c] = 0;
        for (int i = 0; i < 4; i++) {
            int next_r = r + vec_r[i];
            int next_c = c + vec_c[i];            
            dfs(grid, next_r, next_c, maxSize, curSize);
        }
    }
}
class Solution {
    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        int m = heights.length;
        int n = heights[0].length;

        boolean[][] flowsToP = new boolean[m][n];
        boolean[][] flowsToA = new boolean[m][n];

        List<List<Integer>> result = new ArrayList<>();

        for (int r = 0; r < m; r++) {
            dfs(m, n, r, 0, flowsToP, heights[r][0], heights);
            dfs(m, n, r, n - 1, flowsToA, heights[r][n - 1], heights);
        }

        for (int c = 0; c < n; c++) {
            dfs(m, n, 0, c, flowsToP, heights[0][c], heights);
            dfs(m, n, m - 1, c, flowsToA, heights[m - 1][c], heights);
        }

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (flowsToP[i][j] && flowsToA[i][j]) {
                    result.add(new ArrayList<Integer>(List.of(i, j)));
                }
            }
        }

        return result;
    }

    private void dfs(int m, int n, int cur_r, int cur_c, boolean[][] flows, int prevHeight, int[][] heights) {
        if (cur_r < 0 || cur_r >= m || cur_c < 0 || cur_c >= n || prevHeight > heights[cur_r][cur_c] || flows[cur_r][cur_c]) return;
        flows[cur_r][cur_c] = true;
        dfs(m, n, cur_r - 1, cur_c, flows, heights[cur_r][cur_c], heights);
        dfs(m, n, cur_r + 1, cur_c, flows, heights[cur_r][cur_c], heights);
        dfs(m, n, cur_r, cur_c - 1, flows, heights[cur_r][cur_c], heights);
        dfs(m, n, cur_r, cur_c + 1, flows, heights[cur_r][cur_c], heights);
    }
}
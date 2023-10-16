class Solution {
    static ArrayList<Integer>[] graph;
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        int[] visited = new int[numCourses];
        graph = new ArrayList[numCourses];
        for (int i = 0; i < numCourses; i++) {
            graph[i] = new ArrayList<>();
        }
        for (int[] prerequisite : prerequisites) {
            graph[prerequisite[0]].add(prerequisite[1]);
        }
        for (int i = 0; i < numCourses; i++) {
            if (has_cycle(visited, i)) return false;
        }
        return true;
    }

    private static boolean has_cycle(int[] visited, Integer x) {
        if (visited[x] == 1) return true;
        if (visited[x] == 2) return false;
        visited[x] = 1;
        for(Integer node : graph[x]) {
            if (has_cycle(visited, node)) return true;
        }
        visited[x] = 2;
        return false;
    }
}
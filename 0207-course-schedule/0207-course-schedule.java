class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        int[] indegree = new int[numCourses];
        ArrayList<Integer> ans = new ArrayList<>();
        ArrayList<Integer>[] graph = new ArrayList[numCourses];

        for (int i = 0; i < numCourses; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int[] prerequisite : prerequisites) {
            graph[prerequisite[1]].add(prerequisite[0]); // outgoing edge
            indegree[prerequisite[0]]++;
        }

        Queue<Integer> queue = new LinkedList<>();

        for (int i = 0; i < numCourses; i++) {
            if (indegree[i] == 0) queue.add(i);
        }

        while (!queue.isEmpty()) {
            int cur = queue.poll();
            ans.add(cur);
            if (graph[cur] != null) {
                for (int node : graph[cur]) {
                    indegree[node]--;
                    if (indegree[node] == 0) queue.add(node);
                }
            }
        }

        return ans.size() == numCourses;
    }
}
class Solution {
    static ArrayList<Integer>[] graph;
    static Queue<Integer> loopless;
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        Queue<Integer> on_path = new LinkedList<>();
        loopless = new LinkedList<>();
        graph = new ArrayList[numCourses];
        for (int i = 0; i < numCourses; i++) {
            graph[i] = new ArrayList<>();
        }
        for (int[] prerequisite : prerequisites) {
            graph[prerequisite[0]].add(prerequisite[1]);
        }
        for (int i = 0; i < numCourses; i++) {
            if (has_cycle(on_path, i)) return false;
        }
        return true;
    }

    public static boolean has_cycle(Queue<Integer> on_path, Integer x) {
        if (on_path.contains(x)) return true;
        if (loopless.contains(x)) return false;
        on_path.add(x);
        for(Integer node : graph[x]) {
            if (has_cycle(on_path, node)) return true;
        }
        on_path.remove(x);
        loopless.add(x);
        return false;
    }
}
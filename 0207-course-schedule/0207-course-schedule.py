class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [ [] for i in range(numCourses) ]
        indegree = [0] * numCourses
        ans = []

        for pair in prerequisites:
            graph[pair[1]].append(pair[0])
            indegree[pair[0]] += 1

        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            x = queue.popleft()
            ans.append(x)
            for y in graph[x]:
                indegree[y] -= 1
                if indegree[y] == 0:
                    queue.append(y)
            
        return len(ans) == numCourses
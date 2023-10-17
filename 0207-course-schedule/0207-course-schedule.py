class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [ [] for i in range(numCourses) ]
        visited = [0] * numCourses
    
        for pair in prerequisites:
            graph[pair[1]].append(pair[0])   

        def has_cycle(x: int) -> bool:
            if visited[x] == 1: return True
            if visited[x] == 2: return False
            visited[x] = 1
            for y in graph[x]:
                if has_cycle(y):
                    return True
            visited[x] = 2
            return False

        for i in range(numCourses):
            if has_cycle(i):
                return False

        return True
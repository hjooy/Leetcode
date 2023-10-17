class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [ [] for i in range(numCourses) ]
        loopless = set()
        path = set()
        for pair in prerequisites:
            graph[pair[1]].append(pair[0])

        def has_cycle(x: int) -> bool:
            if x in path: return True
            if x in loopless: return False
            path.add(x)
            for y in graph[x]:
                if has_cycle(y):
                    return True
            path.remove(x)
            loopless.add(x)
            return False

        for i in range(numCourses):
            if has_cycle(i):
                return False

        return True
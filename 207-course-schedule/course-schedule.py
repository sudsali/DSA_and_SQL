class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for a,b in prerequisites:
            graph[a].append(b)

        unvisited = 0
        visiting = 1
        visited = 2
        states = [0] * numCourses

        def dfs(node):
            state = states[node]
            if state == visited:
                return True
            elif state == visiting:
                return False
            else:
                states[node] = visiting
                for nei in graph[node]:
                    if not dfs(nei):
                        return False
                states[node] = visited

            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True
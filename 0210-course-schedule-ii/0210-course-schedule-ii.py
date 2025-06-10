class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        if prerequisites == []:
            return [i for i in range(numCourses)]

        for k,v in prerequisites:
            graph[k].append(v)

        unvisited = 0
        visiting = 1
        visited = 2
        states = [unvisited] * numCourses
        ordering = []

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
                ordering.append(node)

            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return list(ordering)
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        res = 0
        for k,v in edges:
            graph[k].append(v)
            graph[v].append(k)
        
        print(graph)
        visited = set()

        def dfs(node):
            visited.add(node)

            for neigh in graph[node]:
                if neigh not in visited:
                    dfs(neigh)
            
        
        for i in range(n):
            if i not in visited:
                dfs(i)
                res+=1
        return res
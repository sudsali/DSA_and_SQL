class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        graph = defaultdict(list)
        web_logs = sorted(zip(timestamp,username,website))

        for t,user,web in web_logs:
            graph[user].append(web)

        scores = defaultdict(set)

        for user,web in graph.items():
            pattern = set(combinations(web,3))
            for i in pattern:
                scores[i].add(user)

        max_count = 0
        res = None
        for pattern,users in scores.items():
            if len(users) > max_count or (max_count == len(users) and (res is None or pattern < res)):
                max_count = len(users)
                res = pattern
        

        return list(res)

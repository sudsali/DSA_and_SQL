class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        newInterval_flag = False

        for i in intervals:
            if i[1] < newInterval[0]:
                res.append(i)
            elif i[0] > newInterval[1]:
                if not newInterval_flag:
                    res.append(newInterval)
                    newInterval_flag = True
                res.append(i)
            else:
                newInterval[0] = min(i[0],newInterval[0])
                newInterval[1] = max(i[1], newInterval[1])

        if not newInterval_flag:
            res.append(newInterval)
            newInterval_flag = True
        return res
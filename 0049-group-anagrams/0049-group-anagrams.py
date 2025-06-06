class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        heap3 = collections.defaultdict(list)
        pattern = set()
        heap2 = {}
        for index, val in enumerate(strs):
            heap2[index] = "".join(sorted(val))
            pattern.add(heap2[index])
    
        i = -1
        for p in pattern:
            i+=1
            for key,val in heap2.items():
                if p == val:
                    heap3[i].append(strs[key])

        res = []
        for key, val in heap3.items():
            res.append(val)
        return res
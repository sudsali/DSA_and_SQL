class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rqueue = []
        dqueue = []
        
        for i, s in enumerate(senate):
            if s == 'R':
                rqueue.append(i)
            else:
                dqueue.append(i)
        
        while rqueue and dqueue:

            r_index = rqueue.pop(0)
            d_index = dqueue.pop(0)
            

            if r_index < d_index:
                rqueue.append(r_index + len(senate)) 
            else:
                dqueue.append(d_index + len(senate)) 
        if rqueue:
            return "Radiant"
        else:
            return "Dire"

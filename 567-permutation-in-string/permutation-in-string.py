class Solution:

    #Use two hashmaps for each string(initailised with counter till len(s1)), 
    # move sliding window for the rest of s2 
    # and increment count for value at r and decrement value at l from s2Count

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count = collections.Counter(s1)
        s2Count = collections.Counter(s2[:len(s1)])

        if s1Count == s2Count:
            return True

        l = 0
        for r in range(len(s1),len(s2)):
            s2Count[s2[r]] += 1
            s2Count[s2[l]] -= 1
            l+=1
            if s1Count == s2Count:
                return True
        return False
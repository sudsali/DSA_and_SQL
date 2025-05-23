class RandomizedSet:

    def __init__(self):
        self.ans = {}
        self.temp = []

    def insert(self, val: int) -> bool:
        if val in self.ans:
            return False
        self.temp.append(val)
        self.ans[val] = len(self.temp) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.temp:
            return False
        j = self.ans[val]
        k = self.temp[-1]

        self.temp[j] = k
        self.ans[k] = j

        self.temp.pop()
        del self.ans[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.temp)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
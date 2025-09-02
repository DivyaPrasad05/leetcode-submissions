class RandomizedSet:

    def __init__(self):
        self.valToInd = {}
        self.numbers = []

    def insert(self, val: int) -> bool:
        # 0. Deal with dups
        if val in self.valToInd:
            return False
        # 1. add number to list
        self.numbers.append(val)
        # 2. get the index of the number
        index = len(self.numbers) - 1
        # 3. add the key value pair to dict
        self.valToInd[val] = index
        return True

    def remove(self, val: int) -> bool:
        # 0. validation if key isnt in dict
        if val not in self.valToInd:
            return False

        # 1. get the index
        index = self.valToInd[val]

        lastVal = self.numbers[-1]

        # swap
        self.numbers[index] = lastVal
        self.valToInd[lastVal] = index

        # 2. Pop from the list
        self.numbers.pop()

        # 3. remove k-v pair from dict
        del self.valToInd[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.numbers)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
"""
k = [bool], index = key
v = [val (int)], index = key
"""
class MyHashMap:

    def __init__(self):
        self.keys = [False] * 1000001
        self.vals = [None] * 1000001

    def put(self, key: int, value: int) -> None:
        self.keys[key] = True
        self.vals[key] = value

    def get(self, key: int) -> int:
        if self.keys[key] == False:
            return -1
        return self.vals[key]

    def remove(self, key: int) -> None:
        self.keys[key] = False
        self.vals[key] = None


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
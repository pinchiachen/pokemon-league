## 2020/10/14

class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.hash_table = dict()
        self.cache_queue = []

    def get(self, key: int) -> int:
        if key not in self.hash_table: return -1
        self.cache_queue.remove(key)
        self.cache_queue.insert(0, key)
        return self.hash_table[key]

    def put(self, key: int, value: int) -> None:
        if key in self.hash_table:
            self.hash_table[key] = value
            self.cache_queue.remove(key)
            self.cache_queue.insert(0, key)
            return
        if (len(self.cache_queue) > self.size):
            return
        if len(self.cache_queue) == self.size:
            pop_key = self.cache_queue.pop()
            self.hash_table.pop(pop_key, None)
        self.cache_queue.insert(0, key)
        self.hash_table[key] = value
        return


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
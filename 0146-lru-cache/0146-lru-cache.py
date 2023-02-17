class LRUCache:

    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.items = {}
    
    def get(self, key: int) -> int:
        if key not in self.items: return -1
        return self.bump(key)
    
    def bump(self, key: int) -> int:
        v = self.items[key]
        del self.items[key]
        self.items[key] = v
        return v
    
    def put(self, key:int, value: int) -> None:
        if key in self.items:
            self.items[key] = value
            self.bump(key)
            return
        
        if len(self.items) == self.capacity:
            del self.items[next(iter(self.items.keys()))] 

        self.items[key] = value

        
    
    
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
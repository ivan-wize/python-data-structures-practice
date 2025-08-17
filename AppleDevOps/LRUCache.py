# =============================================================
# 4) LRU Cache
# Problem:
#   Implement a cache that evicts the least recently used key.
# Example:
#   lru = LRUCache(2); lru.put(1,1); lru.put(2,2); lru.get(1)->1; lru.put(3,3) evicts 2
# =============================================================
class LRUCache:
    def __init__(self, capacity: int):
        self.cap, self.od = capacity, OrderedDict()   # OrderedDict tracks order

    def get(self, key: int) -> int:
        if key not in self.od: return -1
        self.od.move_to_end(key)  # mark as most recent
        return self.od[key]

    def put(self, key: int, value: int) -> None:
        if key in self.od: self.od.move_to_end(key)   # update order if exists
        self.od[key] = value
        if len(self.od) > self.cap:                   # evict least used
            self.od.popitem(last=False)

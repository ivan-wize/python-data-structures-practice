# Problem: LRU Cache (Least Recently Used)
# ----------------------------------------
# Design a data structure for an LRU (Least Recently Used) cache that supports:
#   - get(key) -> value (or -1 if not present)
#   - put(key, value)  # insert/update; evict the least recently used when capacity is full
# All operations must run in O(1) average time.
#
# Requirements:
#   - Capacity is a positive integer.
#   - When a key is accessed (get or put), it becomes the most recently used.
#   - On eviction, remove the least recently used key.
#
# Example:
#   c = LRUCache(2)
#   c.put(1, 1)        # cache = {1:_}
#   c.put(2, 2)        # cache = {1:_, 2:_}
#   c.get(1) -> 1      # 1 becomes most-recent; order: [2 is LRU, 1 is MRU]
#   c.put(3, 3)        # evicts 2; cache keys: {1,3}
#   c.get(2) -> -1
#   c.put(4, 4)        # evicts 1; cache keys: {3,4}
#   c.get(1) -> -1
#   c.get(3) -> 3
#   c.get(4) -> 4

class _Node:
    __slots__ = ("k", "v", "prev", "next")
    def __init__(self, k=0, v=0):
        self.k, self.v = k, v
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.map = {}                 # key -> _Node
        # Dummy head/tail to avoid edge checks
        self.head, self.tail = _Node(), _Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    # ----- small DLL helpers (all O(1)) -----
    def _add_front(self, node: _Node):
        """Insert node right after head (mark as most-recent)."""
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def _remove(self, node: _Node):
        """Unlink node from the list."""
        p, n = node.prev, node.next
        p.next = n
        n.prev = p

    def _move_to_front(self, node: _Node):
        """Mark node as most-recent by moving it to the front."""
        self._remove(node)
        self._add_front(node)

    def _evict_lru(self):
        """Remove least-recently-used node (node before tail)."""
        lru = self.tail.prev
        self._remove(lru)
        del self.map[lru.k]

    # ----- public API -----
    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.map[key]
        self._move_to_front(node)     # access -> most recent
        return node.v

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.v = value            # update
            self._move_to_front(node)
            return
        # new key
        node = _Node(key, value)
        self.map[key] = node
        self._add_front(node)
        if len(self.map) > self.cap:
            self._evict_lru()


# ---- quick sanity test ----
if __name__ == "__main__":
    c = LRUCache(2)
    c.put(1, 1)
    c.put(2, 2)
    assert c.get(1) == 1      # use 1 -> MRU
    c.put(3, 3)               # evict 2
    assert c.get(2) == -1
    c.put(4, 4)               # evict 1
    assert c.get(1) == -1
    assert c.get(3) == 3
    assert c.get(4) == 4
    print("LRU basic tests passed.")

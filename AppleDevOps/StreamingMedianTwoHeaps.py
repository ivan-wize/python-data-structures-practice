# =============================================================
# 8) Streaming Median (Two Heaps)
# Problem:
#   Maintain a data stream; return median at any point.
# Example: add [1,2,3,4] -> median=2.5
# =============================================================
class MedianFinder:
    def __init__(self):
        self.low, self.high = [], []          # max-heap(low), min-heap(high)

    def add_num(self, num: int) -> None:
        if not self.low or num <= -self.low[0]:  # goes to low half
            heapq.heappush(self.low, -num)
        else:
            heapq.heappush(self.high, num)
        # balance heaps (size diff <= 1)
        if len(self.low) > len(self.high)+1:
            heapq.heappush(self.high, -heapq.heappop(self.low))
        elif len(self.high) > len(self.low):
            heapq.heappush(self.low, -heapq.heappop(self.high))

    def find_median(self) -> float:
        if len(self.low) > len(self.high):    # odd total -> root of low
            return float(-self.low[0])
        return (-self.low[0] + self.high[0]) / 2.0  # even -> avg roots
    
# =============================================================
# 3) Token-Bucket Rate Limiter
# Problem:
#   Allow N requests per second with a bucket of given capacity.
#   Tokens refill at rate_per_sec up to capacity.
# Example:
#   rl = RateLimiter(2,2); rl.allow(0.0) -> True (uses a token)
# =============================================================
class RateLimiter:
    def __init__(self, rate_per_sec: float, capacity: int):
        self.rate, self.capacity = float(rate_per_sec), int(capacity)
        self.tokens, self.last = float(capacity), 0.0  # start full

    def allow(self, now: float) -> bool:
        # Refill tokens based on elapsed time since last call
        if now > self.last:
            self.tokens = min(self.capacity, self.tokens + (now - self.last) * self.rate)
            self.last = now
        # Consume a token if available
        if self.tokens >= 1.0:
            self.tokens -= 1.0
            return True
        return False

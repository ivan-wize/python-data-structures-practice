# =============================================================
# 9) Exponential Backoff Retry Decorator
# Problem:
#   Retry a function on exception with exponential delays.
# Example:
#   @retry(3,0.1,ValueError) -> tries 3 times with backoff.
# =============================================================
def retry(max_attempts: int, base_delay: float, exc: Type[Exception], _sleep=time.sleep) -> Callable:
    def deco(fn: Callable) -> Callable:
        def wrapper(*args, **kwargs):
            attempt = 1
            while True:
                try:
                    return fn(*args, **kwargs)        # try function
                except exc:                           # caught exception
                    if attempt >= max_attempts: raise # out of attempts
                    _sleep(base_delay * (2 ** (attempt-1)))  # backoff
                    attempt += 1
        return wrapper
    return deco

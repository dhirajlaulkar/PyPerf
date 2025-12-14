import functools
import time

def fibonacci_naive(n: int) -> int:
    """
    Recursive Fibonacci without caching.
    Exponential time complexity: O(2^n).
    Very slow for n > 35.
    """
    if n < 2:
        return n
    return fibonacci_naive(n - 1) + fibonacci_naive(n - 2)

@functools.lru_cache(maxsize=None)
def fibonacci_cached(n: int) -> int:
    """
    Recursive Fibonacci with LRU Cache.
    Linear time complexity: O(n) due to memoization.
    """
    if n < 2:
        return n
    return fibonacci_cached(n - 1) + fibonacci_cached(n - 2)

def expensive_operation_simulation(arg: int) -> int:
    """
    Simulates a heavy computation or I/O callback.
    """
    time.sleep(0.1) # Simulate 100ms latency
    return arg * 2

# Manual caching example
_cache = {}
def expensive_operation_with_manual_cache(arg: int) -> int:
    if arg in _cache:
        return _cache[arg]
    
    result = expensive_operation_simulation(arg)
    _cache[arg] = result
    return result

@functools.lru_cache(maxsize=128)
def expensive_operation_lru(arg: int) -> int:
    return expensive_operation_simulation(arg)

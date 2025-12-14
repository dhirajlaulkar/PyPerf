import timeit
from typing import Callable

def time_function(func: Callable, loops: int = 1000, *args, **kwargs) -> float:
    """
    Times a function execution over a number of loops.
    Returns the average time per execution in seconds.
    """
    # Create a wrapper lambda to handle args
    wrapped_func = lambda: func(*args, **kwargs)
    
    total_time = timeit.timeit(wrapped_func, number=loops)
    avg_time = total_time / loops
    
    print(f"Function '{func.__name__}' averaged {avg_time:.9f} seconds over {loops} runs.")
    return avg_time

def compare_functions(func1: Callable, func2: Callable, loops: int = 1000) -> None:
    """
    Compares two functions using timeit.
    """
    print(f"--- Benchmarking {func1.__name__} vs {func2.__name__} ({loops} runs) ---")
    t1 = time_function(func1, loops=loops)
    t2 = time_function(func2, loops=loops)
    
    if t1 < t2:
        faster = func1.__name__
        ratio = t2 / t1
    else:
        faster = func2.__name__
        ratio = t1 / t2
        
    print(f"\nResult: {faster} is {ratio:.2f}x faster.")

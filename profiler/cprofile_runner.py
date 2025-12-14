import cProfile
import pstats
import io
from typing import Callable, Any

def profile_function(func: Callable, *args, **kwargs) -> Any:
    """
    Runs a function with cProfile and prints a cumulative report.
    Returns the return value of the function.
    """
    pr = cProfile.Profile()
    pr.enable()
    result = func(*args, **kwargs)
    pr.disable()
    
    s = io.StringIO()
    # Sort by cumulative time to show what took the most time
    ps = pstats.Stats(pr, stream=s).sort_stats('cumulative')
    ps.print_stats()
    
    print(s.getvalue())
    return result

class ProfilerContext:
    """
    Context manager for profiling a block of code.
    """
    def __init__(self, name: str = "Block"):
        self.name = name
        self.pr = cProfile.Profile()

    def __enter__(self):
        self.pr.enable()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.pr.disable()
        print(f"\n--- Profiling Report: {self.name} ---")
        s = io.StringIO()
        ps = pstats.Stats(self.pr, stream=s).sort_stats('cumulative')
        ps.print_stats()
        print(s.getvalue())

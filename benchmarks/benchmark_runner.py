import random
import timeit
from typing import Dict, Any, List, Callable
from pyperf.optimizations import naive_vs_optimized
from pyperf.optimizations import caching_examples

def run_benchmark(
    name: str,
    naive_func: Callable,
    optimized_func: Callable,
    setup_func: Callable[[], tuple],
    loops: int = 100
) -> Dict[str, Any]:
    """
    Runs a benchmark comparing two functions.
    setup_func: Should return a tuple of (args, kwargs) to pass to the functions.
    """
    args, kwargs = setup_func()
    
    # Pre-bind arguments for fair timing
    n_func = lambda: naive_func(*args, **kwargs)
    o_func = lambda: optimized_func(*args, **kwargs)
    
    t_naive = timeit.timeit(n_func, number=loops)
    t_optimized = timeit.timeit(o_func, number=loops)
    
    avg_naive = t_naive / loops
    avg_optimized = t_optimized / loops
    improvement = avg_naive / avg_optimized if avg_optimized > 0 else float('inf')
    
    return {
        "benchmark": name,
        "loops": loops,
        "naive_time_sec": avg_naive,
        "optimized_time_sec": avg_optimized,
        "improvement_factor": improvement
    }

def run_all_benchmarks():
    results = []
    
    # 1. Find Common Elements
    def setup_common_elements():
        l1 = [random.randint(0, 1000) for _ in range(1000)]
        l2 = [random.randint(0, 1000) for _ in range(1000)]
        return (l1, l2), {}
    
    results.append(run_benchmark(
        "Common Elements (List vs Set)",
        naive_vs_optimized.find_common_elements_naive,
        naive_vs_optimized.find_common_elements_optimized,
        setup_common_elements,
        loops=100
    ))

    # 2. Sum of Squares
    def setup_sum_squares():
        return (1000000,), {}

    results.append(run_benchmark(
        "Sum of Squares (Loop vs Formula)",
        naive_vs_optimized.calculate_sum_of_squares_naive,
        naive_vs_optimized.calculate_sum_of_squares_optimized,
        setup_sum_squares,
        loops=100
    ))

    # 3. Find Duplicates
    def setup_duplicates():
        data = [random.randint(0, 500) for _ in range(1000)]
        return (data,), {}
        
    results.append(run_benchmark(
        "Find Duplicates (List vs Set)",
        naive_vs_optimized.find_duplicates_naive,
        naive_vs_optimized.find_duplicates_optimized,
        setup_duplicates,
        loops=100
    ))

    # 4. Fibonacci (Caching)
    def setup_fib():
        return (30,), {} # 30 is high enough to show difference, but not hang naive too long
        
    results.append(run_benchmark(
        "Fibonacci(30) (Recursive vs LRU Cache)",
        caching_examples.fibonacci_naive,
        caching_examples.fibonacci_cached,
        setup_fib,
        loops=5 # Fewer loops as naive fib is slow
    ))

    # Print Results Table
    print(f"{'Benchmark':<40} | {'Naive (s)':<12} | {'Optimized (s)':<12} | {'Improvement':<12}")
    print("-" * 85)
    for r in results:
        print(f"{r['benchmark']:<40} | {r['naive_time_sec']:.9f} | {r['optimized_time_sec']:.9f} | {r['improvement_factor']:.2f}x")
    
    return results

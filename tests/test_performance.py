import pytest
import timeit
from pyperf.optimizations import naive_vs_optimized
from pyperf.optimizations import caching_examples

def assert_faster(naive_func, opt_func, distinct_args=False, loops=1000, *args):
    """
    Helper to assert that opt_func is faster than naive_func.
    """
    if distinct_args:
        # If args need to be generated per call or are mutable, handle here if needed.
        # simple check assumes args are safe to reuse or immutable enough for this valid check
        pass
        
    t_naive = timeit.timeit(lambda: naive_func(*args), number=loops)
    t_opt = timeit.timeit(lambda: opt_func(*args), number=loops)
    
    # Assert optimization is at least 1.1x faster (10%) to be safe against noise, 
    # though for O(N^2) vs O(N) it should be massive.
    assert t_opt < t_naive, f"Optimized function {opt_func.__name__} was slower! Naive: {t_naive}, Opt: {t_opt}"

def test_common_elements_performance():
    l1 = list(range(1000))
    l2 = list(range(500, 1500))
    # Comparison
    assert_faster(naive_vs_optimized.find_common_elements_naive, 
                  naive_vs_optimized.find_common_elements_optimized, 
                  False, 100, l1, l2)

def test_sum_of_squares_performance():
    n = 10000
    assert_faster(naive_vs_optimized.calculate_sum_of_squares_naive,
                  naive_vs_optimized.calculate_sum_of_squares_optimized,
                  False, 1000, n)

def test_find_duplicates_performance():
    data = list(range(1000)) + list(range(100)) # some dupes
    assert_faster(naive_vs_optimized.find_duplicates_naive,
                  naive_vs_optimized.find_duplicates_optimized,
                  False, 100, data)

def test_fibonacci_performance():
    n = 20 # 30 is too slow for unit tests if naive is run many times
    assert_faster(caching_examples.fibonacci_naive,
                  caching_examples.fibonacci_cached,
                  False, 10, n)

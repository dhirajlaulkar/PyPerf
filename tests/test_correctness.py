import pytest
from pyperf.optimizations import naive_vs_optimized
from pyperf.optimizations import caching_examples

def test_find_common_elements():
    l1 = [1, 2, 3, 4, 5, 2]
    l2 = [4, 5, 6, 7, 8, 4]
    expected = [4, 5]
    
    # Naive correctness
    assert naive_vs_optimized.find_common_elements_naive(l1, l2) == expected
    # Optimized correctness
    assert naive_vs_optimized.find_common_elements_optimized(l1, l2) == expected
    # Compare both
    assert naive_vs_optimized.find_common_elements_optimized(l1, l2) == naive_vs_optimized.find_common_elements_naive(l1, l2)

def test_sum_of_squares():
    n = 10
    # 0^2 + 1^2 + ... + 9^2 = 285
    expected = 285
    assert naive_vs_optimized.calculate_sum_of_squares_naive(n) == expected
    assert naive_vs_optimized.calculate_sum_of_squares_optimized(n) == expected

def test_find_duplicates():
    data = [1, 2, 3, 2, 4, 5, 5, 1]
    expected = [1, 2, 5]
    assert naive_vs_optimized.find_duplicates_naive(data) == expected
    assert naive_vs_optimized.find_duplicates_optimized(data) == expected

def test_fibonacci():
    n = 10
    expected = 55
    assert caching_examples.fibonacci_naive(n) == expected
    assert caching_examples.fibonacci_cached(n) == expected

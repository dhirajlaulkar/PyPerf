from typing import List

def find_common_elements_naive(list1: List[int], list2: List[int]) -> List[int]:
    """
    Finds common elements between two lists using nested loops.
    Time Complexity: O(n * m)
    """
    common = []
    # Inefficient: O(n*m) if not using `in` optimally, but even `in` on a list is O(n).
    # Here we iterate and check existence in another list.
    for item in list1:
        if item in list2:
            common.append(item)
    return sorted(list(set(common))) # converting to set to remove duplicates if any, then sorting for stability

def find_common_elements_optimized(list1: List[int], list2: List[int]) -> List[int]:
    """
    Finds common elements using sets.
    Time Complexity: O(n + m) (average case for set construction and intersection)
    """
    set1 = set(list1)
    set2 = set(list2)
    # Set intersection is very optimized in CPython
    common = set1.intersection(set2)
    return sorted(list(common))

def calculate_sum_of_squares_naive(n: int) -> int:
    """
    Calculates sum of squares from 0 to n-1 using a loop.
    """
    result = 0
    for i in range(n):
        result += i * i
    return result

def calculate_sum_of_squares_optimized(n: int) -> int:
    """
    Calculates sum of squares using a mathematical formula.
    Sum of k^2 for k=0 to n-1 is: ((n-1) * n * (2n - 1)) / 6
    Direct calculation: O(1)
    """
    # Adjust for n-1 because naive loop is range(n) -> 0..n-1
    limit = n - 1
    if limit < 0: return 0
    return (limit * (limit + 1) * (2 * limit + 1)) // 6

def find_duplicates_naive(data: List[int]) -> List[int]:
    """
    Finds duplicates using a list to track seen elements.
    O(n^2) because 'if item in seen' is O(len(seen)).
    """
    seen = []
    duplicates = []
    for item in data:
        if item in seen:
            if item not in duplicates:
                duplicates.append(item)
        else:
            seen.append(item)
    return sorted(duplicates)

def find_duplicates_optimized(data: List[int]) -> List[int]:
    """
    Finds duplicates using a set to track seen elements.
    O(n) average case.
    """
    seen = set()
    duplicates = set()
    for item in data:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return sorted(list(duplicates))

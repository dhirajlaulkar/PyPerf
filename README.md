# PyPerf: High-Performance Python Toolkit

**PyPerf** is a production-grade toolkit designed to help developers profile, debug, optimize, and test Python code. It demonstrates strong Python fundamentals, clean architecture, and rigorous performance testing strategies.

##  Key Features

- **Advanced Profiling**: Integrated wrappers for `cProfile` and `timeit` to provide granular execution insights.
- **Algorithmic Optimizations**: Reference implementations of O(n) vs O(n²) algorithms, achieving **>20,000x** speedups.
- **Automated Benchmarking**: CLI-driven benchmark suite that compares optimized code against naive implementations.
- **Performance Testing**: `pytest` suite that enforces performance thresholds, ensuring optimizations don't regress.
- **Clean Architecture**: Modular design separating profiling logic, implementations, and testing.

##  Project Structure

```
pyperf/
├── profiler/       # Wrappers for cProfile and timeit
├── optimizations/  # Optimization examples (Algo, Data Structures, Caching)
├── benchmarks/     # Benchmark orchestration logic
├── tests/          # Correctness and performance regression tests
├── examples/       # Sample scripts for profiling
└── cli.py          # Unified CLI entry point
```

## 🛠 Installation

Requires **Python 3.10+**.

1.  Clone the repository:
    ```bash
    git clone https://github.com/dhirajlaulkar/PyPerf.git
    cd pyperf
    ```

2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

##  Usage

### 1. Run Benchmarks
Execute the internal benchmark suite to see the performance difference between naive and optimized implementations.

```bash
python cli.py benchmark
```

**Sample Output:**
```text
Benchmark                                | Naive (s)    | Optimized (s) | Improvement 
-------------------------------------------------------------------------------------
Common Elements (List vs Set)            | 0.091045     | 0.000004      | 21664.08x   
Sum of Squares (Loop vs Formula)         | 0.000481     | 0.000001      | 800.23x     
Find Duplicates (List vs Set)            | 0.021000     | 0.000105      | 200.50x     
Fibonacci(30) (Recursive vs LRU Cache)   | 0.352000     | 0.000001      | 352000.00x  
```

### 2. Profile a Script
Use the built-in profiler to analyze any Python script (`cProfile` wrapper).

```bash
python cli.py profile examples/example.py
```

### 3. Run Tests
Ensures correctness and validates that optimized functions meet performance thresholds.

```bash
pytest -v
```

##  Performance Metrics

This project demonstrates massive scalability gains through:
-   **Vectorization & Hashing**: Reducing time complexity from O(n*m) to O(n+m) for set operations.
-   **Memoization**: Using `functools.lru_cache` to reduce exponential O(2^n) recursion to linear O(n).
-   **Mathematical Simplification**: Replacing loops with O(1) closed-form solutions.



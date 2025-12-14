import argparse
import sys
import runpy
import os
from pyperf.benchmarks import benchmark_runner
from pyperf.profiler import cprofile_runner

def main():
    parser = argparse.ArgumentParser(description="PyPerf: Performance Profiling & Benchmarking Toolkit")
    subparsers = parser.add_subparsers(dest="command", help="Available subcommands")
    
    # Profile Subcommand
    profile_parser = subparsers.add_parser("profile", help="Run cProfile on a python script")
    profile_parser.add_argument("script", help="Path to the python script to profile")
    
    # Benchmark Subcommand
    subparsers.add_parser("benchmark", help="Run internal benchmark suite")
    
    args = parser.parse_args()
    
    if args.command == "profile":
        script_path = args.script
        if not os.path.exists(script_path):
            print(f"Error: Script '{script_path}' not found.")
            sys.exit(1)
            
        print(f"Running cProfile on: {script_path}")
        # We use runpy to execute the script in the current process but with stats wrapped
        # However, to use cprofile_runner we pass a callable. 
        # runpy.run_path is a callable but it might not handle globals purely nicely if not careful.
        # Alternatively, cProfile.run(exec(...)) is standard.
        
        # Let's use cProfile directly or our wrapper if adaptable. 
        # Our wrapper `profile_function` expects a callable.
        # Let's make a callable that runs the script.
        
        def run_script():
            # We must be careful about sys.argv and __main__
            # Save original argv
            old_argv = sys.argv
            sys.argv = [script_path]
            try:
                runpy.run_path(script_path, run_name="__main__")
            except Exception as e:
                print(f"Error running script: {e}")
            finally:
                sys.argv = old_argv

        cprofile_runner.profile_function(run_script)
        
    elif args.command == "benchmark":
        print("Running PyPerf Implementation Benchmarks...")
        benchmark_runner.run_all_benchmarks()
        
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

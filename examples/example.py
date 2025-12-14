import time

def slow_function():
    print("Starting slow function...")
    total = 0
    for i in range(1000000):
        total += i
    print("Finished slow function.")
    return total

def main():
    slow_function()

if __name__ == "__main__":
    main()

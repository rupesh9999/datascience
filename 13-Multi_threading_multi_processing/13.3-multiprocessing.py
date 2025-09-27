# What is multiprocessing:
# Multiprocessing is a way to achieve true parallelism in Python by running multiple processes independently.
# Each process has its own Python interpreter and memory space, meaning they don't share memory directly
# (unlike threads). This allows multiprocessing to bypass the Global Interpreter Lock (GIL),
# making it suitable for CPU-bound tasks where you want to utilize multiple CPU cores.

# When to use multiprocessing:
# Multiprocessing is ideal for CPU-bound tasks, such as heavy computations, data processing,
# or scientific simulations, where the program spends most of its time performing calculations.
# By distributing these tasks across multiple processes, you can leverage the full power of
# multi-core processors, significantly speeding up execution.
# It can also be used for I/O-bound tasks, but multithreading is often simpler to implement
# for those scenarios if the GIL is not a concern.

import multiprocessing
import time

def print_numbers():
    for i in range(5):
        print(f"Number: {i}")
        time.sleep(1)

def print_letters():
    for letter in 'ABCDE':
        print(f"Letter: {letter}")
        time.sleep(2)

if __name__ == "__main__":
    start_time = time.time()

    # Create 2 processes
    p1 = multiprocessing.Process(target=print_numbers)
    p2 = multiprocessing.Process(target=print_letters)

    # Start the processes
    p1.start()
    p2.start()

    # Wait for the processes to complete
    p1.join()
    p2.join()

    finished_time = time.time() - start_time
    print(f"Finished in {finished_time:.2f} seconds")

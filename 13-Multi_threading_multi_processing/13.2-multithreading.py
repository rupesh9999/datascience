# When to use multi-threading:
# Multi-threading is suitable for I/O-bound tasks, where the program spends a lot of time waiting for external operations
# like reading/writing files, network requests, or user input. In such cases, while one thread is waiting,
# another thread can execute, improving overall program responsiveness and throughput.
# It's generally not ideal for CPU-bound tasks in Python due to the Global Interpreter Lock (GIL),
# which limits true parallel execution of Python bytecode across multiple CPU cores.
# For CPU-bound tasks, multi-processing is often a better choice.

import threading
import time

def print_numbers():
    for i in range(5):
        print(f"Number: {i}")
        time.sleep(1)

def print_letters():
    for letter in 'ABCDE':
        print(f"Letter: {letter}")
        time.sleep(2)

## create 2 threads

t1=threading.Thread(target=print_numbers)
t2=threading.Thread(target=print_letters)

t1.start()
t2.start()

## wait for the threads to complete
t1.join()
t2.join()


finished_time = time.time()-t
print(finished_time)

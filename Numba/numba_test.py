import time
from numba import jit


def without_numba(x):
    k = 0
    start_time = time.perf_counter()
    for i in range(1, x):
        k += 1
    end_time = time.perf_counter()
    total_time = end_time - start_time
    print(k + 1)
    return total_time


@jit(nopython=True)
def with_numba(x):
    k = 0
    for i in range(1, x):
        k += 1
    print(k + 1)


print("executing functions...")

BILLION = 1_000_000_000
large_int = 1 * BILLION
print(f"Without Numba time 1: {without_numba(large_int)}")
# print(f"Without Numba time 2: {without_numba(large_int)}")
# print(f"Without Numba time 3: {without_numba(large_int)}")
print("\n")

start_time = time.perf_counter()
with_numba(large_int)
end_time = time.perf_counter()
print(f"With Numba time 1: {end_time-start_time}")

start_time = time.perf_counter()
with_numba(large_int)
end_time = time.perf_counter()
print(f"With Numba time 2: {end_time-start_time}")

start_time = time.perf_counter()
with_numba(large_int)
end_time = time.perf_counter()
print(f"With Numba time 3: {end_time-start_time}")

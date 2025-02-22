"""Big O Graph Visualizer"""

import random
import time
import matplotlib.pyplot as plt

from bigo import (
    length_of_longest_substring_n3,
    length_of_longest_substring_n2,
    length_of_longest_substring_n,
)


# Function to generate a random string of length n
def generate_random_string(n: int) -> str:
    """
    Generates a random string of a given length based on the characters given.
    """
    return "".join(
        random.choices(
            "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMnOPQRSTUVWXYZ0123456789 !@#$%^&*()_+-=",
            k=n,
        )
    )


# Lists to store input sizes and runtimes for each function
input_sizes = []
times_n3 = []
times_n2 = []
times_n = []
SKIP_N3 = SKIP_N2 = SKIP_N = False

# Test with increasing input sizes
for size in range(0, 10001, 200):
    if SKIP_N3 and SKIP_N2 and SKIP_N:
        break
    input_sizes.append(size)
    TEST_STRING = generate_random_string(size)

    if not SKIP_N3:
        start_time = time.time()
        length_of_longest_substring_n3(TEST_STRING)
        total_time = time.time() - start_time
        times_n3.append(total_time)
        if total_time > 2:
            SKIP_N3 = True

    if not SKIP_N2:
        start_time = time.time()
        length_of_longest_substring_n2(TEST_STRING)
        total_time = time.time() - start_time
        times_n2.append(total_time)
        if total_time > 2:
            SKIP_N2 = True

    if not SKIP_N:
        start_time = time.time()
        length_of_longest_substring_n(TEST_STRING)
        total_time = time.time() - start_time
        times_n.append(total_time)
        if total_time > 2:
            SKIP_N = True


# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(input_sizes[: len(times_n3)], times_n3, label="O(N^3)", marker="o")
plt.plot(input_sizes[: len(times_n2)], times_n2, label="O(N^2)", marker="s")
plt.plot(input_sizes, times_n, label="O(N)", marker="^")
plt.xlabel("Input Size (Length of String)")
plt.ylabel("Time (seconds)")
plt.title("Runtime Comparison of length_of_longest_substring Functions")
plt.legend()
plt.grid(True)
plt.show()

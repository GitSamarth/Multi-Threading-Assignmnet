import numpy as np
import time
import multiprocessing as mp
import matplotlib.pyplot as plt
import psutil

MATRIX_SIZE = 1000
NUM_MATRICES = 200

constant_matrix = np.random.rand(MATRIX_SIZE, MATRIX_SIZE)


def multiply_matrix(_):
    matrix = np.random.rand(MATRIX_SIZE, MATRIX_SIZE)
    result = np.matmul(matrix, constant_matrix)
    return result


def run_threads(num_threads):
    start = time.time()

    with mp.Pool(num_threads) as pool:
        pool.map(multiply_matrix, range(NUM_MATRICES))

    end = time.time()
    return (end - start) / 60


if __name__ == "__main__":

    threads = []
    times = []
    cpu_usage = []

    print("Testing Threads 1 to 12\n")

    for t in range(1, 13):

        print(f"Running with {t} threads...")

        time_taken = run_threads(t)

        cpu = psutil.cpu_percent(interval=1)

        threads.append(t)
        times.append(time_taken)
        cpu_usage.append(cpu)

        print(f"Time Taken: {time_taken:.2f} minutes")
        print(f"CPU Usage: {cpu}%\n")

    # Execution Time Graph
    plt.figure()
    plt.plot(threads, times, marker='o')
    plt.xlabel("Number of Threads")
    plt.ylabel("Time (Minutes)")
    plt.title("Execution Time vs Threads")
    plt.grid(True)
    plt.savefig("execution_graph.png")

    # CPU Usage Graph (LIKE YOUR IMAGE)
    plt.figure()
    plt.plot(threads, cpu_usage, marker='o')
    plt.xlabel("Number of Threads")
    plt.ylabel("CPU Usage (%)")
    plt.title("CPU Usage vs Threads")
    plt.grid(True)
    plt.savefig("cpu_usage_vs_threads.png")

    plt.show()
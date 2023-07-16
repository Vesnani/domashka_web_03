from multiprocessing import cpu_count, Pool
import logging
from timeit import default_timer


def factorize_num(n):
    divisors = []
    for m in range(1, n+1):
        if n % m == 0:
            divisors.append(m)
    return divisors


def factorize(*numbers_input):
    numbers_output = []
    start_time = default_timer()
    for n in numbers_input:
        divisors_list = factorize_num(n)
        numbers_output.append(divisors_list)
    end_time = default_timer()
    runtime = end_time - start_time
    return numbers_output, runtime


def multi_factorize(*numbers_input):
    pool = Pool(cpu_count())
    start_time = default_timer()
    result = pool.map(factorize_num, numbers_input)
    pool.close()
    pool.join()
    end_time = default_timer()
    runtime = end_time - start_time
    return result, runtime

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')

    sync_results, sync_runtime = factorize(128, 255, 99999, 10651060)
    print(f"Synchronous results: {sync_results}, execution time {sync_runtime} seconds")

    parallel_results, parallel_runtime = multi_factorize(128, 255, 99999, 10651060)
    print(f"Parallel results: {parallel_results}, execution time {parallel_runtime} seconds")


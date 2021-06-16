import time


def take_time(func):
    start = time.time()
    func()
    end = time.time()
    return end - start


def big_comp():
    sum = 1
    for i in range(10000000):
        sum += i


run_time = take_time(big_comp)
print(run_time)

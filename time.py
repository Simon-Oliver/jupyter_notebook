import time
import concurrent.futures


def log(i):
    time.sleep(2)
    print("Log", i)


with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    for i in range(15):
        executor.submit(log, i)

print("----------- End -----------")

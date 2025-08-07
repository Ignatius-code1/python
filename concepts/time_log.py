import time


def counter():
    for n in range (1,10000):

        print(n)
        time.sleep(0.1)

        start_time = time.time()
        counter()
        end_time = time.time()

        diff = end_time - start_time
        print(f"Counter took {diff} seconds to run")
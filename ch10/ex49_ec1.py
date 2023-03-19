import time
from math import ceil
 
def elapsed_since(data, min_delta):
    last_time = None
    for item in data:
        current_time = time.perf_counter()
        delta = current_time - (last_time
                                or current_time)
        if delta < min_delta:
            time.sleep(ceil(min_delta-delta))
            current_time = time.perf_counter()
            delta = current_time - (last_time
                                    or current_time)
        last_time = time.perf_counter()
        yield (delta, item)
 
for t in elapsed_since('abcd', 5):
    print(t)
    time.sleep(2)

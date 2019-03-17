import time
import numpy as np

def test(seq):
    start_time = time.time()
    for i in range(100):
        for j in range(100):
            seq[i] = seq[i] + seq[j]

    print(time.time() - start_time)

p = [1]*1000
n = np.array(p)

test(p)
test(n)
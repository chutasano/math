import sys
from nt import c
import numpy as np
import signal

BASE = 10
STOP = 10**9

# let -1 denote a C-small number, c(n) < n
# let 0 denote a C number, c(n) = n
# let 1 denote a C-big number, c(n) > n
if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal.default_int_handler)
    start = 0
    try:
        t = np.load(str(BASE) + ".npy")
        start = t.shape[0]
        if t.shape[0] >= STOP:
            print("already completed")
            sys.exit(0)
        else:
            z = np.zeros(STOP-t.shape[0], dtype=np.int8)
            t = np.concatenate( (t, z), axis=0)
    except IOError:
        t = np.zeros(STOP, dtype=np.int8)
    counter = 0
    for i in range(start, STOP):
        try:
            k = c(i, BASE)
            if k > i:
                t[i] = -1
            elif k == i:
                t[i] = 0
                counter += 1
            else:
                t[i] = 1
        except KeyboardInterrupt:
            print("Interrupted at " + str(i-1))
            print("Found " + str(counter) + " C numbers")
            t = t[:i-1]
            np.save(str(BASE), t)
    print("Completed")
    print("Found " + str(counter) + " C numbers")
    np.save(str(BASE), t)


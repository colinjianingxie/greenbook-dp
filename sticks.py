import numpy as np
import time

def break_stick(stick_length=1, breaks=2, get_type='min'):

    s = np.random.uniform(0, stick_length, breaks) # stick breaks
    s = np.sort(s)
    parts = np.empty(breaks+1)
    parts[0] = s[0]
    for i in range(1, len(s)):
        parts[i] = (s[i]-s[i-1])
    parts[-1] = (1-s[-1])
    parts = np.sort(parts)
    if get_type == 'min':
        return parts[0]
    else:
        return parts[-1]

def simulate(n, p):
    counter = 0
    for i in range(n):
        res = break_stick(1, 2, 'min')
        #print(res)
        if res <= p:
            counter += 1
    return counter/n

def ensemble(m):
    res = np.empty(m)
    for i in range(m):
        res[i] = (simulate(10000, 0.2))
    return np.mean(res)

def main():

    start = time.time()
    print(ensemble(1000))
    end = time.time()
    print(21/25)
    print(end - start)

main()

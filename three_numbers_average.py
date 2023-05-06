from random import *

def ensemble_repeat(m, n):
    average = []
    for i in range(m):
        average.append(simulate_repeat(n))
    return sum(average) / m
def simulate_repeat(n):
    counter = 0
    for i in range(n):
        a = randint(1, 20)
        b = randint(1, 20)
        c = randint(1, 20)
        if (a + b == 2*c):
            counter += 1
        elif a + c == 2*b:
            counter += 1
        elif b + c == 2*a:
            counter += 1
    return counter / n

def simulate_no_repeat(n):
    counter = 0
    for i in range(n):
        a, b, c = sample(range(1, 21), 3)
        if (a + b == 2*c):
            counter += 1
        elif a + c == 2*b:
            counter += 1
        elif b + c == 2*a:
            counter += 1
    return counter / n

def possible_combinations_2():
    possible_set = set()
    c = 0
    for i in range(1, 21):
        for j in range(1, 21):
            for k in range(1, 21):
                possible_set.add((i,j,k))
                if i + j == 2 * k:
                    c += 1
                elif i + k == 2 * j:
                    c += 1
                elif j + k == 2 * i:
                    c += 1
    print(len(possible_set))
    print(c / len(possible_set))
    print(20*19*3)

def possible_combinations():
    possible_set = set()
    c = 0
    for i in range(1, 21):
        for j in range(1, 21):
            for k in range(1, 21):
                possible_set.add((i,j,k))
                if i + j == 2 * k:
                    c += 1
                elif i + k == 2 * j:
                    c += 1
                elif j + k == 2 * i:
                    c += 1
    print(len(possible_set))
    print(c / len(possible_set))
    print(20*19*3)
def main():
    #print(simulate_repeat(10000))
    #print(ensemble_repeat(10000, 10000))
    #possible_combinations()
    print(simulate_no_repeat(1000000) * 1140)
main()

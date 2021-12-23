#!/usr/bin/env python
from itertools import combinations
import math
import bisect
import sys

def power_set(List):
    PS = [list(j) for i in range(len(List)) for j in combinations(List, i+1)]
    return PS

def main():
    if len(sys.argv) < 2:
        print('Usage: ./shapley.py <filename>')
        return

    characteristic_function = []

    with open(sys.argv[1]) as gamefile:
        for line in gamefile:
            try:
                n = int(line[line.index('=') + 1:])
            except:
                print("Invalid file format")
                sys.exit(0)
            break
        for line in gamefile:
            characteristic_function = line.strip().split(",")

    if n == 0:
        print("No players, exiting")
        sys.exit(0)

    tempList = list([i for i in range(n)])
    N = power_set(tempList)

    shapley_values = []
    for i in range(n):
        shapley = 0
        for j in N:
            if i not in j:
                cmod = len(j)
                Cui = j[:]
                bisect.insort_left(Cui,i)
                l = N.index(j)
                k = N.index(Cui)
                temp = float(float(characteristic_function[k]) - float(characteristic_function[l])) *\
                           float(math.factorial(cmod) * math.factorial(n - cmod - 1)) / float(math.factorial(n))
                shapley += temp
          

        cmod = 0
        Cui = [i]
        k = N.index(Cui)
        temp = float(characteristic_function[k]) * float(math.factorial(cmod) * math.factorial(n - cmod - 1)) / float(math.factorial(n))
        shapley += temp

        shapley_values.append(shapley)

    print(shapley_values)

if __name__ == '__main__':
    main()
# https://www.spoj.com/problems/PRIME1/

import numpy


def sieve_of_erastosthenes():
    max = 999999937 - 2
    sqrt_max = 31623
    primes = numpy.ones(max + 1, dtype=numpy.bool_)  # primes[0] --> 2, prime[max] --> 100000000

    # start = time.time()
    # list = list(range(2, sqrt_max+1))
    # [ for number in list if primes[number-2]]

    # map(sieve, tuple(range(2, sqrt_max+1)))
    for number in range(2, sqrt_max + 1):
        if primes[number - 2]:
            primes[(number * number - 2):max:number] = False
    # end = time.time()
    # print("Durée", end-start)

    return primes


array = sieve_of_erastosthenes()
t = int(input())

for i in range(0, t):
    a, b = [int(x) for x in input().split(sep=" ")]

    if a == 1:
        a = 2
    if b > 999999937:
        b = 999999937

    x = a - 2
    while x <= b - 2:
        if array[x]:
            print(x + 2)
        x = x + 1
    print()

# https://www.spoj.com/problems/PRIME1/
# https://zestedesavoir.com/forums/sujet/9288/mon-aventure-sur-spoj-et-autres-codeforces/?page=3

import bisect
import math
import sys
import time


def prime_sieve(end):
    nb = [False, False] + [True] * (end - 1)  # 0 and 1 to False

    nb[2**2::2] = [False] * int(math.ceil((len(nb) - 4) / 2))

    for i in range(3, math.ceil(math.sqrt(len(nb)))):
        if nb[i]:
            nb[i**2::2*i] = [False] * math.ceil((len(nb)-i*i) / (2*i))

    return [n for n, is_prime in enumerate(nb) if is_prime]


def main():
    nb_test = int(sys.stdin.readline())
    cases = []
    max_end = 0
    for e in range(nb_test):
        start, end = map(int, sys.stdin.readline().split(" "))
        cases.append({"start": start, "end": end})
        if max_end < end:
            max_end = end

    primes = prime_sieve(math.ceil(math.sqrt(max_end)))

    for case in cases:
        start, end = case["start"], case["end"]
        if start == 1:
            if end >= 2:
                start = 2
            else:
                print()
                continue

        nb = [True] * (end - start + 1)

        max_p = bisect.bisect(primes, math.sqrt(end))
        min_p = bisect.bisect_left(primes, start)

        [print(i) for i in primes[min_p:max_p]]  # cette ligne permet d'afficher les nombres premiers entre start et sqrt(end)

        for p in primes[:max_p]:
            try:
                first = next(filter(lambda i: (start + i) % p == 0,
                                    range(len(nb))
                                    )
                             )
                nb[first::p] = [False] * len(nb[first::p])  # Parce qu'ici ils seront mis à False
            except StopIteration:
                break

        [print(i) for i, is_prime in enumerate(nb, start=start) if is_prime]

        print()  # New line and each test case


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print("durée", end-start)
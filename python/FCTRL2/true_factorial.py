# https://www.spoj.com/problems/FCTRL2/

import math

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t -= 1
        n = int(input())
        print(math.factorial(n))

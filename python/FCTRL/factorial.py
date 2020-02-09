# https://www.spoj.com/problems/FCTRL/

if __name__ == '__main__':
    t = int(input())

    while t > 0:
        t -= 1
        n = int(input())
        trailing_zero = n // 5
        x = 25
        while x <= n:
            trailing_zero += n // x
            x = x * 5
        print(trailing_zero)

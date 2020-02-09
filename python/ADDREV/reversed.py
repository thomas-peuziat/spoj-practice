# https://www.spoj.com/problems/ADDREV/

if __name__ == '__main__':
    n = int(input())

    for _ in range(0, n):
        a, b = [int(x[::-1]) for x in input().split(sep=" ")]
        sol = a + b
        sol_reversed = int(str(sol)[::-1])
        print(sol_reversed)

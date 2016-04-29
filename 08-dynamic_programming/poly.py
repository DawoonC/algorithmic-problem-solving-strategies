# Problem ID: POLY
# https://algospot.com/judge/problem/read/POLY
# timeout

from collections import defaultdict

def readline():
    return raw_input()


def get_num_of_poly(n, first, polydict, MOD):
    if n == first:
        return 1
    result = polydict[(n,first)]
    if result != -1:
        return result
    result = 0
    for second in range(1, n-first+1):
        add = second + first - 1
        add *= get_num_of_poly(n-first, second, polydict, MOD)
        add %= MOD
        result += add
        result %= MOD
        polydict[(n,first)] = result
    return result


def get_total_poly(n, polydict, MOD):
    result = 0
    for first in range(1, n+1):
        result += get_num_of_poly(n, first, polydict, MOD)
    return result % MOD


def poly():
    MOD = 10*1000*1000
    total_tests = int(readline())
    for testcase in range(total_tests):
        n = int(readline())
        polydict = defaultdict(lambda:-1)
        print get_total_poly(n, polydict, MOD)


if __name__ == '__main__':
    poly()  # run
# coding=utf-8
# Problem ID: POLY
# https://algospot.com/judge/problem/read/POLY

from collections import defaultdict
MOD = 10*1000*1000

def poly(n, first, cache):
    if n == first:
        return 1

    ret = cache[n, first]
    if ret != -1:
        return ret

    ret = 0
    for second in range(1, n-first+1):
        add = second + first -1
        add *= poly(n-first, second, cache)
        add %= MOD
        ret += add
        ret %= MOD
        cache[n, first] = ret

    return ret



def runner():
    total_tests = int(raw_input())
    for testcase in range(total_tests):
        n = int(raw_input())
        cache = defaultdict(lambda:-1)
        result = 0
        for first in range(1, n+1):
            result += poly(n, first, cache)
        print result
runner()
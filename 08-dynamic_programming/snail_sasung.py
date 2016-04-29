# coding=utf-8
# Problem ID: SNAIL
# https://algospot.com/judge/problem/read/SNAIL

from collections import defaultdict

def snail(days, climbed, n, m, cache):
    if days == m:
        if climbed >= n:
            return 1
        else:
            return 0

    ret = cache[days, climbed]
    if ret != -1:
        return ret

    ret = 0.75 * float(snail(days+1, climbed+2, n, m, cache)) + 0.25 * float(snail(days+1, climbed+1, n, m, cache))
    cache[days, climbed] = ret
    return ret



def runner():
    total_tests = int(raw_input())
    for testcase in range(total_tests):
        cache = defaultdict(lambda:-1)
        n, m = map(int, raw_input().split())
        result = snail(1, 1, n, m, cache)
        print result

runner()
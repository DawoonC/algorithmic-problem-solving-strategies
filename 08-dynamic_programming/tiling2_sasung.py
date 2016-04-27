# coding=utf-8
# Problem ID: TILING2
# https://algospot.com/judge/problem/read/TILING2

from collections import defaultdict
MOD = 1000000007

def tiling2(width, cache):
    if width <= 1:
        return 1

    ret = cache[width]
    if ret != -1:
        return ret

    ret = cache[width] = (tiling2(width - 2, cache) + tiling2(width - 1, cache)) % MOD
    return ret

def runner():
    total_tests = int(raw_input())
    for testcase in range(total_tests):
        width = int(raw_input())
        cache = defaultdict(lambda:-1)
        print tiling2(width, cache)

runner()
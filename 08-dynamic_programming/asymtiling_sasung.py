# coding=utf-8
# Problem ID: ASYMTILING
# https://algospot.com/judge/problem/read/ASYMTILING

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

def asymmetric(width, cache):
    if width % 2 == 1:
        return (tiling2(width, cache) - tiling2(width/2, cache) + MOD) % MOD

    else:
        ret = tiling2(width, cache)
        ret = (ret - tiling2(width/2, cache) + MOD) % MOD
        ret = (ret - tiling2((width/2)-1, cache) + MOD) % MOD
        return ret

def asymmetric2(width, cache):
    if width <= 2:
        return 0

    ret = asymmetric2(width-2, cache) % MOD
    ret = (ret + asymmetric2(width-4, cache) % MOD)
    ret = (ret + tiling2(width-3, cache) % MOD)
    ret = (ret + tiling2(width-3, cache) % MOD)

    return ret

def runner():
    total_tests = int(raw_input())
    for testcase in range(total_tests):
        width = int(raw_input())
        cache = defaultdict(lambda:-1)
        print asymmetric(width, cache)

# runner()

'''
3
2
4
92
'''
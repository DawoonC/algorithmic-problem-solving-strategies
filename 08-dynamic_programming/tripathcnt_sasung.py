# coding=utf-8
# Problem ID: TRIPATHCNT
# https://algospot.com/judge/problem/read/TRIPATHCNT

from collections import defaultdict

def path2(n, y, x, triangle, cache_path):

    if(y == n-1):
        return triangle[y][x]

    ret = cache_path[y,x]

    if ret != -1:
        return ret

    ret = cache_path[y,x] = max(path2(n, y+1, x, triangle, cache_path), path2(n, y+1, x+1, triangle, cache_path) + triangle[y][x])

    return ret



def tripathcnt(n, triangle, y, x, cache_tripathcnt, cache_path):
    if y == n - 1:
        return 1

    ret = cache_tripathcnt[y,x]

    if ret!= -1:
        return ret

    ret = 0
    if path2(n, y+1, x+1, triangle, cache_path) >= path2(n, y+1, x, triangle, cache_path):
        ret += tripathcnt(n, triangle, y+1, x+1, cache_tripathcnt, cache_path)
        cache_tripathcnt[y,x] = ret
    if path2(n, y+1, x+1, triangle, cache_path) <= path2(n, y+1, x, triangle, cache_path):
        ret += tripathcnt(n, triangle, y+1, x, cache_tripathcnt, cache_path)
        cache_tripathcnt[y,x] = ret

    return ret


def runner():
    total_tests = int(raw_input())
    for testcase in range(total_tests):
        cache_tripathcnt = defaultdict(lambda:-1)
        cache_path = defaultdict(lambda:-1)
        n = int(raw_input())
        triangle = []
        for i in range(n):
            triangle.append([int(x) for x in raw_input().split()])
        print tripathcnt(n, triangle, 0, 0, cache_tripathcnt, cache_path)

runner()
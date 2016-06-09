# coding=utf-8
# Problem ID: RUNNINGMEDIAN
# https://algospot.com/judge/problem/read/RUNNINGMEDIAN

from heapq import heappush, heappop

def median(n, a, b, max_heap, min_heap, next):
    A = lambda : (next * a + b) % 20090711
    ret = next
    max_heap.append(-1 * next)
    for i in range(1, n):
        next = A()
        if len(min_heap) == len(max_heap):
            heappush(max_heap, -1 * next)
        else:
            heappush(min_heap, next)
        if min_heap[0] < -1 * max_heap[0]:
            heappush(max_heap, -1 * heappop(min_heap))
            heappush(min_heap, -1 * heappop(max_heap))
        ret += -1 * max_heap[0]
        ret %= 20090711
    return ret


def runner():
    total_tests = int(raw_input())
    for testcase in range(total_tests):
        n, a, b = map(int, raw_input().split())
        next = 1983
        min_heap = list()
        max_heap = list()
        print median(n, a, b, max_heap, min_heap, next)

runner()
#
'''
3
10 1 0
10 1 1
10000 1273 4936
'''
# Problem ID: RUNNINGMEDIAN
# https://algospot.com/judge/problem/read/RUNNINGMEDIAN
# 796ms

import heapq

def readline():
    return raw_input()


def get_next_input(last_input, a, b):
    return (last_input * a + b) % 20090711


def get_median_sum(n, a, b):
    last_input = 1983
    median_sum = [last_input]
    min_heap = []  # for larger half
    max_heap = [last_input]  # for smaller half
    for i in xrange(1, n):
        next_input = get_next_input(last_input, a, b)
        if i % 2 == 0:
            heapq.heappush(max_heap, -next_input)
        else:
            heapq.heappush(min_heap, next_input)
        if abs(max_heap[0]) > min_heap[0]:
            _max = abs(heapq.heappop(max_heap))
            _min = heapq.heappop(min_heap)
            heapq.heappush(max_heap, -_min)
            heapq.heappush(min_heap, _max)
        median_sum[0] += abs(max_heap[0])
        last_input = next_input
    return median_sum[0] % 20090711


def runningmedian():
    total_tests = int(readline())
    for testcase in range(total_tests):
        n, a, b = map(int, readline().split())
        print get_median_sum(n, a, b)


if __name__ == '__main__':
    runningmedian()  # run

# Problem ID: STRJOIN
# https://algospot.com/judge/problem/read/STRJOIN
# took 20ms

import heapq


def readline():
    return raw_input()


def get_min_join_iter(str_lengths):
    sorted_lengths = sorted(str_lengths)
    total = 0
    while len(sorted_lengths) > 1:
        joined = sorted_lengths.pop(0) + sorted_lengths.pop(0)
        sorted_lengths.append(joined)
        sorted_lengths.sort()
        total += joined
    return total


def get_min_join_iter_w_heap(str_lengths):
    heapq.heapify(str_lengths)
    total = 0
    while len(str_lengths) > 1:
        joined = heapq.heappop(str_lengths) + heapq.heappop(str_lengths)
        heapq.heappush(str_lengths, joined)
        total += joined
    return total


def strjoin():
    total_tests = int(readline())
    for testcase in range(total_tests):
        readline()
        str_lengths = map(int, readline().split())
        result = get_min_join_iter_w_heap(str_lengths)
        print result


if __name__ == '__main__':
    strjoin()  # run

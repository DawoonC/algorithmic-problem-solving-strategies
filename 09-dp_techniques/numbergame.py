# Problem ID: NUMBERGAME
# https://algospot.com/judge/problem/read/NUMBERGAME
# took 136ms

from collections import defaultdict


def readline():
    return raw_input()


def get_score_diff(left, right, numbers, cache):
    if left == right:
        return 0
    result = cache[(left, right)]
    if result is not None:
        return result
    take_left = numbers[left] - get_score_diff(left + 1, right, numbers, cache)
    take_right = numbers[right - 1] - get_score_diff(left, right - 1, numbers, cache)
    remove_left, remove_right = -float('inf'), -float('inf')
    if right - left > 1:
        remove_left = 0 - get_score_diff(left + 2, right, numbers, cache)
        remove_right = 0 - get_score_diff(left, right - 2, numbers, cache)
    result = cache[(left, right)] = max(take_left, take_right, remove_left, remove_right)
    return result


def numbergame():
    total_tests = int(readline())
    for testcase in range(total_tests):
        n = int(readline())
        numbers = map(int, readline().split())
        cache = defaultdict(lambda: None)
        result = get_score_diff(0, n, numbers, cache)
        print result


if __name__ == '__main__':
    numbergame()  # run

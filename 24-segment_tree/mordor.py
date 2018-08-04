# Problem ID: MORDOR
# https://algospot.com/judge/problem/read/MORDOR
# took > 5000ms

from range_minimum_query import RangeMinQuery


def readline():
    return raw_input()


def get_level(start, end, range_min, range_max):
    max_h = -range_max.query(start, end)
    min_h = range_min.query(start, end)
    return max_h - min_h


def mordor():
    total_tests = int(readline())
    for testcase in range(total_tests):
        n_signs, n_paths = map(int, readline().split())
        heights = map(int, readline().split())
        range_min = RangeMinQuery(heights)
        range_max = RangeMinQuery([-h for h in heights])
        for _ in range(n_paths):
            start_sign, end_sign = map(int, readline().split())
            print get_level(start_sign, end_sign, range_min, range_max)


if __name__ == '__main__':
    mordor()  # run

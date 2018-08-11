# Problem ID: SORTGAME
# https://algospot.com/judge/problem/read/SORTGAME
# took 1184ms

from collections import defaultdict


def readline():
    return raw_input()


def precalc(n):
    ordered_nums = tuple(i for i in xrange(n))
    queue = []
    queue.append(ordered_nums)
    sort_dict = defaultdict(lambda: None)
    sort_dict[ordered_nums] = 0
    while queue:
        here = queue.pop(0)
        cost = sort_dict[here]
        for i in xrange(n):
            for j in xrange(i + 2, n + 1):
                _next = here[:i] + here[i:j][::-1] + here[j:]
                if sort_dict[_next] is None:
                    sort_dict[_next] = cost + 1
                    queue.append(_next)
    return sort_dict


def convert_nums(unsorted_nums, n):
    sorted_nums = sorted(unsorted_nums)
    i_dict = {sorted_nums[i]: i for i in xrange(n)}
    return tuple(i_dict[e] for e in unsorted_nums)


def sortgame():
    total_tests = int(readline())
    max_n = 8
    answer_dict = {}
    for n in xrange(1, max_n + 1):
        answer_dict[n] = precalc(n)
    for testcase in xrange(total_tests):
        n = int(readline())
        sort_dict = answer_dict[n]
        nums = map(int, readline().split())
        converted_nums = convert_nums(nums, n)
        print sort_dict[converted_nums]


if __name__ == '__main__':
    sortgame()  # run

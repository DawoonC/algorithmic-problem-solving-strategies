# Problem ID: SORTGAME
# https://algospot.com/judge/problem/read/SORTGAME
# timeout

from collections import defaultdict

def readline():
    return raw_input()


def precalc(n):
    ordered_nums = tuple(i for i in xrange(n))
    queue = []
    queue.append(ordered_nums)
    sort_dict = defaultdict(lambda:-1)
    sort_dict[ordered_nums] = 0
    while len(queue) != 0:
        here = queue.pop(0)
        cost = sort_dict[here]
        for i in range(n):
            for j in range(i+2, n+1):
                _next = tuple(here[:i]+here[i:j][::-1]+here[j:])
                if sort_dict[_next] == -1:
                    sort_dict[_next] = cost + 1
                    queue.append(_next)
    return sort_dict


def convert_nums(unsorted_nums, n):
    converted_nums = [None] * n
    for i in range(n):
        converted = 0
        for j in range(n):
            if unsorted_nums[j] < unsorted_nums[i]:
                converted += 1
        converted_nums[i] = converted
    return tuple(converted_nums)


def sortgame():
    total_tests = int(readline())
    for testcase in range(total_tests):
        n = int(readline())
        nums = map(int, readline().split())
        sort_dict = precalc(n)
        converted_nums = convert_nums(nums, n)
        print sort_dict[converted_nums]


if __name__ == '__main__':
    sortgame()  # run

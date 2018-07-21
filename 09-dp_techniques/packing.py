# Problem ID: PACKING
# https://algospot.com/judge/problem/read/PACKING
# took 1760ms
# similar to Knapsack problem

from collections import defaultdict


def readline():
    return raw_input()


def get_max_score(size_limit, item, n, items, cache):
    if item == n:
        return 0
    result = cache[(item, size_limit)]
    if result is not None:
        return result
    # skip current item
    result = get_max_score(size_limit, item + 1, n, items, cache)
    name, size, score = items[item]
    if size <= size_limit:
        # select current item
        result = max(result, get_max_score(size_limit - size, item + 1, n, items, cache) + score)
    cache[(item, size_limit)] = result
    return result


def get_choices(size_limit, item, n, items, cache, choices):
    if item == n:
        return choices
    a = get_max_score(size_limit, item + 1, n, items, cache)
    b = get_max_score(size_limit, item, n, items, cache)
    if a == b:
        return get_choices(size_limit, item + 1, n, items, cache, choices)
    choices.add(item)
    name, size, score = items[item]
    return get_choices(size_limit - size, item + 1, n, items, cache, choices)


def packing():
    total_tests = int(readline())
    for testcase in range(total_tests):
        n, size_limit = map(int, readline().split())
        items = []
        for _ in range(n):
            name, size, score = readline().split()
            items.append((name, int(size), int(score)))
        cache = defaultdict(lambda: None)
        max_score = get_max_score(size_limit, 0, n, items, cache)
        choices = get_choices(size_limit, 0, n, items, cache, set())
        print max_score, len(choices)
        for e in choices:
            print items[e][0]


if __name__ == '__main__':
    packing()  # run

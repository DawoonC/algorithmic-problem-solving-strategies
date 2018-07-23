# Problem ID: SUSHI
# https://algospot.com/judge/problem/read/SUSHI
# took > 8000ms
# similar to Knapsack problem


def readline():
    return raw_input()


# recursive approach makes too much recursion depth
# and uses too much memory
def get_max_preference_w_recursion(budget, n, items, cache):
    result = cache[budget]
    if result is not None:
        return result
    result = 0
    for i in range(n):
        price, preference = items[i]
        if price <= budget:
            candidate = preference + get_max_preference(budget - price, n, items, cache)
            result = max(result, candidate)
    cache[budget] = result
    return result


def get_max_preference(budget, n, items):
    result = 0
    cache = [0] * 201
    for sub_budget in xrange(1, budget + 1):
        candidate = 0
        for i in xrange(n):
            price, preference = items[i]
            if price <= sub_budget:
                temp = cache[(sub_budget - price) % 201] + preference
                candidate = max(candidate, temp)
        cache[sub_budget % 201] = candidate
        result = max(result, candidate)
    return result


def sushi():
    total_tests = int(readline())
    for testcase in range(total_tests):
        n, budget = map(int, readline().split())
        budget = budget / 100
        items = []
        for _ in range(n):
            price, preference = map(int, readline().split())
            items.append((price / 100, preference))
        max_preference = get_max_preference(budget, n, items)
        print max_preference


if __name__ == '__main__':
    sushi()  # run

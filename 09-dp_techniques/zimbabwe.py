# Problem ID: ZIMBABWE
# https://algospot.com/judge/problem/read/ZIMBABWE
# took > 2000ms

from itertools import permutations
from collections import defaultdict


def readline():
    return raw_input()


# with all permutations < egg_price, without dp
def get_prev_price_count(egg_price, m, lowest_price):
    count = 0
    perms = permutations(lowest_price, len(lowest_price))
    dup = set()
    for e in perms:
        temp = ''.join(e)
        if temp in dup:
            continue
        if temp >= egg_price:
            break
        if int(temp) % m == 0:
            count += 1
            dup.add(temp)
    return count


# with dp
def price(index, taken, mod, less, egg_price, m, digits, cache):
    if index == len(digits):
        return 1 if less and mod == 0 else 0
    result = cache[(taken, mod, less)]
    if result is not None:
        return result
    result = 0
    for i in range(len(digits)):
        if (taken & (1 << i)) == 0:
            if not less and egg_price[index] < digits[i]:
                continue
            if i > 0 and digits[i - 1] == digits[i] and (taken & (1 << (i - 1))) == 0:
                continue
            next_taken = taken | (1 << i)
            next_mod = (mod * 10 + int(digits[i])) % m
            next_less = less or egg_price[index] > digits[i]
            result += price(index + 1, next_taken, next_mod, next_less, egg_price, m, digits, cache)
            result %= 1000000007
    cache[(taken, mod, less)] = result
    return result


def zimbabwe():
    total_tests = int(readline())
    for testcase in range(total_tests):
        egg_price, m = readline().split()
        m = int(m)
        lowest_price = ''.join(sorted(egg_price))
        if egg_price == lowest_price:
            print 0
            continue
        # print get_prev_price_count(egg_price, m, lowest_price)
        cache = defaultdict(lambda: None)
        print price(0, 0, 0, False, egg_price, m, lowest_price, cache)


if __name__ == '__main__':
    zimbabwe()  # run

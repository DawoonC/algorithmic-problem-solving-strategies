# Problem ID: CHILDRENDAY
# https://algospot.com/judge/problem/read/CHILDRENDAY

from collections import defaultdict

def readline():
    return raw_input()


def add_digit(here, edge, mod):
    there = here * 10 + edge
    if there >= mod:
        return (there % mod) + mod
    return there % mod


def get_gifts(digits, n, m):
    sorted_digits = sorted(int(d) for d in str(digits))
    digits_len = len(sorted_digits)
    parent = defaultdict(lambda: -1)
    choice = defaultdict(lambda: -1)
    queue = []
    parent[0] = 0
    queue.append(0)
    while len(queue) != 0:
        here = queue.pop(0)
        for i in range(digits_len):
            there = add_digit(here, sorted_digits[i], n)
            if parent[there] == -1:
                parent[there] = here
                choice[there] = sorted_digits[i]
                queue.append(there)
    if parent[n + m] == -1:
        return 'IMPOSSIBLE'
    result = ''
    here = n + m
    while parent[here] != here:
        result += str(choice[here])
        here = parent[here]
    return result[::-1]


def childrenday():
    total_tests = int(readline())
    for testcase in range(total_tests):
        digits, n, m = map(int, readline().split())
        result = get_gifts(digits, n, m)
        print result


if __name__ == '__main__':
    childrenday()  # run

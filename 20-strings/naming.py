# Problem ID: NAMING
# https://algospot.com/judge/problem/read/NAMING
# took > 500ms

from get_partial_match import get_partial_match


def readline():
    return raw_input()


def get_prefix_suffix(s):
    result = []
    pi = get_partial_match(s)
    k = len(s)
    while k > 0:
        result.append(k)
        k = pi[k - 1]
    return result


def naming():
    name_1 = readline()
    name_2 = readline()
    s = name_1 + name_2
    lengths = get_prefix_suffix(s)
    for i in xrange(len(lengths) - 1, -1, -1):
        print lengths[i],
    print


if __name__ == '__main__':
    naming()  # run

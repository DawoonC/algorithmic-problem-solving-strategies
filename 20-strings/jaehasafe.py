# Problem ID: JAEHASAFE
# https://algospot.com/judge/problem/read/JAEHASAFE
# took > 1000ms

from get_max_overlap import get_max_overlap


def readline():
    return raw_input()


def jaehasafe():
    total_tests = int(readline())
    for testcase in range(total_tests):
        n = int(readline())
        states = []
        result = 0
        for i in xrange(n + 1):
            states.append(readline())
            if i == 0:
                continue
            elif i % 2 == 0:
                result += get_max_overlap(states[i], states[i - 1])
            else:
                result += get_max_overlap(states[i - 1], states[i])
        print result


if __name__ == '__main__':
    jaehasafe()  # run

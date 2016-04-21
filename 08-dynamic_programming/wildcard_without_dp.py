# Problem ID: WILDCARD
# https://algospot.com/judge/problem/read/WILDCARD
# took 35ms

import re

def readline():
    return raw_input()


def check_pattern(regex, words):
    matched = [word for word in words if regex.sub('', word) == '']
    matched.sort()
    for word in matched:
        print word


def wildcard():
    total_tests = int(readline())
    for testcase in range(total_tests):
        pattern = readline()
        regex = re.compile(pattern.replace('*', '.*').replace('?', '.'))
        total_words = int(readline())
        words = []
        for i in range(total_words):
            words.append(readline())
        check_pattern(regex, words)


if __name__ == '__main__':
    wildcard()  # run
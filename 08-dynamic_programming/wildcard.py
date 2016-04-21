# Problem ID: WILDCARD
# https://algospot.com/judge/problem/read/WILDCARD
# took 169ms

from collections import defaultdict

def readline():
    return raw_input()


def check_pattern(pattern, words):
    matched = []
    for word in words:
        matchdict = defaultdict(lambda:-1)
        if match(0, 0, pattern, word, matchdict):
            matched.append(word)
    matched.sort()
    for word in matched:
        print word


def match(i, j, w, s, matchdict):
    if matchdict[(i,j)] != -1:
        return matchdict[(i,j)]
    if i < len(w) and j < len(s) and (w[i] == '?' or w[i] == s[j]):
        result = matchdict[(i+1,j+1)] = match(i+1, j+1, w, s, matchdict)
        return result
    if i == len(w):
        result = matchdict[(i,j)] = j == len(s)
        return result
    if w[i] == '*':
        if match(i+1, j, w, s, matchdict):
            result = matchdict[(i+1,j)] = 1
            return result
        if j < len(s) and match(i, j+1, w, s, matchdict):
            result = matchdict[(i,j+1)] = 1
            return result
    matchdict[(i,j)] = 0
    return 0


def wildcard():
    total_tests = int(readline())
    for testcase in range(total_tests):
        pattern = readline()
        total_words = int(readline())
        words = []
        for i in range(total_words):
            words.append(readline())
        check_pattern(pattern, words)


if __name__ == '__main__':
    wildcard()  # run
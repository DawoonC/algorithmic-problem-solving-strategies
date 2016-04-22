# Problem ID: WILDCARD
# https://algospot.com/judge/problem/read/WILDCARD
from collections import defaultdict

def check_pattern(pattern, words):
    matched = []
    for word in words:
        cache = defaultdict(lambda:-1)
        print('start', cache)
        if matchMemoized(0, 0, pattern, word, cache):
            matched.append(word)
    matched.sort()
    for word in matched:
        print word

def matchMemoized(w, s, pattern, word, cache):
    if cache[(w,s)] != -1:
        return cache[(w,s)]

    while(w < len(pattern) and s < len(word) and (pattern[w] == '?' or pattern[w] == word[s])):
        result = cache[(w+1, s+1)] = matchMemoized(w+1, s+1, pattern, word, cache)
        print(result, cache)
        return result

    if w == len(pattern):
        result = cache[(w, s)] = s == len(word)
        return result

    if(pattern[w] == '*'):
        if matchMemoized(w+1, s, pattern, word, cache):
            result = cache[(w+1, s)] = 1
            return result
        if s < len(word) and matchMemoized(w, s+1, pattern, word, cache):
            result = cache[(w, s+1)] = 1
            return result

    cache[(w, s)] = 0
    return 0

check_pattern("he*p", ['heap', 'help', 'helpp'])

def wildcard():
    total_tests = int(raw_input())
    for testcase in range(total_tests):
        pattern = raw_input()
        total_words = int(raw_input())
        words = []
        for i in range(total_words):
            words.append(raw_input())
        check_pattern(pattern, words)


# wildcard()
# Problem ID: RESTORE
# https://algospot.com/judge/problem/read/RESTORE
# took 24ms

from collections import defaultdict


def readline():
    return raw_input()


def overlap(a, b):
    l = min(len(a), len(b))
    while l > 0:
        if a[-l:] == b[:l]:
            return l
        l -= 1
    return l


def preprocess(words, k):
    filtered = []
    for i in range(k):
        skip = False
        for j in range(k):
            if i != j and words[i] in words[j]:
                skip = True
        if not skip:
            filtered.append(i)
    return [words[i] for i in filtered]


def get_overlaps(words, k):
    overlaps = defaultdict(lambda: defaultdict(lambda: None))
    for i in range(k):
        for j in range(k):
            if i != j:
                overlaps[i][j] = overlap(words[i], words[j])
    return overlaps


def get_max_overlap(w, taken, words, k, overlaps, cache):
    if all(taken):
        return 0
    result = cache[(w, str(taken))]
    if result is not None:
        return result
    for next_w in range(k):
        if taken[next_w]:
            continue
        elif w != next_w:
            taken[next_w] = 1
            curr_overlap = overlaps[w][next_w] if w != -1 else 0
            candidate = curr_overlap + get_max_overlap(next_w, taken, words, k, overlaps, cache)
            taken[next_w] = 0
            result = max(result, candidate)
    cache[(w, str(taken))] = result
    return result


def get_shortest_concat(w, taken, words, k, overlaps, cache):
    if all(taken):
        return ''
    for next_w in range(k):
        if taken[next_w]:
            continue
        elif w != next_w:
            taken[next_w] = 1
            curr_overlap = overlaps[w][next_w] if w != -1 else 0
            if_used = curr_overlap + get_max_overlap(next_w, taken, words, k, overlaps, cache)
            taken[next_w] = 0
            if get_max_overlap(w, taken, words, k, overlaps, cache) == if_used:
                taken[next_w] = 1
                concat = (words[next_w][overlaps[w][next_w]:] +
                          get_shortest_concat(next_w, taken, words, k, overlaps, cache))
                taken[next_w] = 0
                return concat
    return ''


def restore():
    total_tests = int(readline())
    for testcase in range(total_tests):
        k = int(readline())
        temp = []
        for _ in range(k):
            temp.append(readline().strip())
        words = preprocess(temp, k)
        if len(words) == 1:
            print words[0]
            continue
        overlaps = get_overlaps(words, len(words))
        taken = [0] * len(words)
        cache = defaultdict(lambda: None)
        get_max_overlap(-1, taken, words, len(words), overlaps, cache)
        print get_shortest_concat(-1, taken, words, k, overlaps, cache)


if __name__ == '__main__':
    restore()  # run

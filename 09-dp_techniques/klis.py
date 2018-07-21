# Problem ID: KLIS
# https://algospot.com/judge/problem/read/KLIS
# took 1580ms

from collections import defaultdict

CONSTANTS = {
    'MAX': 2000000000 + 1,
}


def readline():
    return raw_input()


def get_lis(start, seq, n, cache):
    result = cache[start + 1]
    if result is not None:
        return result
    result = 1
    for i in range(start + 1, n):
        if start == -1 or seq[start] < seq[i]:
            result = cache[start + 1] = max(result, get_lis(i, seq, n, cache) + 1)
    return result


def count_lis(start, seq, n, length_cache, count_cache):
    if get_lis(start, seq, n, length_cache) == 1:
        return 1
    result = count_cache[start + 1]
    if result is not None:
        return result
    result = 0
    for i in range(start + 1, n):
        if (start == -1 or seq[start] < seq[i]) and get_lis(start, seq, n, length_cache) == get_lis(i, seq, n, length_cache) + 1:
            next_count = count_lis(i, seq, n, length_cache, count_cache)
            result = count_cache[start + 1] = min(CONSTANTS['MAX'], result + next_count)
    return result


def get_kth_lis(start, skip, kth, seq, n, length_cache, count_cache):
    if start != -1:
        kth.append(seq[start])
    followers = []
    for i in range(start + 1, n):
        if (start == -1 or seq[start] < seq[i]) and get_lis(start, seq, n, length_cache) == get_lis(i, seq, n, length_cache) + 1:
            followers.append((seq[i], i))
    followers.sort()
    for i in range(len(followers)):
        index = followers[i][1]
        cnt = count_lis(index, seq, n, length_cache, count_cache)
        if cnt <= skip:
            skip -= cnt
        else:
            get_kth_lis(index, skip, kth, seq, n, length_cache, count_cache)
            break


def klis():
    total_tests = int(readline())
    for testcase in range(total_tests):
        n, k = map(int, readline().split())
        seq = map(int, readline().split())
        length_cache = defaultdict(lambda: None)
        count_cache = defaultdict(lambda: None)
        length_result = get_lis(-1, seq, n, length_cache) - 1
        print length_result
        kth = []
        get_kth_lis(-1, k - 1, kth, seq, n, length_cache, count_cache)
        print ' '.join(map(str, kth))


if __name__ == '__main__':
    klis()  # run

# Problem ID: PI
# https://algospot.com/judge/problem/read/PI
# maximum recursion depth exceeded

from collections import defaultdict

def classify(start, end, numbers):
    sub_numbers = numbers[start:end+1]
    if sub_numbers == (sub_numbers[0]*len(sub_numbers)):
        return 1
    progressive = True
    for i in range(len(sub_numbers)-1):
        if int(sub_numbers[i+1]) - int(sub_numbers[i]) != int(sub_numbers[1]) - int(sub_numbers[0]):
            progressive = False
    if progressive and abs(int(sub_numbers[1]) - int(sub_numbers[0])) == 1:
        return 2
    alternating = True
    for i in range(len(sub_numbers)):
        if sub_numbers[i] != sub_numbers[i%2]:
            alternating = False
    if alternating:
        return 4
    if progressive:
        return 5
    return 10


def memorize(start, numbers, cache):
    if start >= len(numbers):
        return 0
    result = cache[start]
    if result != -1:
        return result
    result = float('inf')
    for i in range(3, 6):
        result = cache[start+i] = min(result, memorize(start+i, numbers, cache) + classify(start, start+i-1, numbers))
    return result


def pi():
    total_tests = int(raw_input())
    for testcase in range(total_tests):
        numbers = raw_input()
        cache = defaultdict(lambda:-1)
        print memorize(0, numbers, cache)


pi()
# Problem ID: PI
# https://algospot.com/judge/problem/read/PI
# maximum recursion depth exceeded

from collections import defaultdict

def readline():
    return raw_input()


def classify(start, end, numbers):
    sub_numbers = numbers[start:end+1]
    # score 1: same numbers
    if sub_numbers == (sub_numbers[0]*len(sub_numbers)):
        return 1
    # score 2: incrementing/decrementing by 1
    progressive = True
    for i in range(len(sub_numbers)-1):
        if int(sub_numbers[i+1]) - int(sub_numbers[i]) != int(sub_numbers[1]) - int(sub_numbers[0]):
            progressive = False
    if progressive and abs(int(sub_numbers[1]) - int(sub_numbers[0])) == 1:
        return 2
    # score 4: two numbers are alternating
    alternating = True
    for i in range(len(sub_numbers)):
        if sub_numbers[i] != sub_numbers[i%2]:
            alternating = False
    if alternating:
        return 4
    # score 5: incrementing/decrementing pattern
    if progressive:
        return 5
    # score 10: default case
    return 10


def memorize(start, numbers, numbers_length, pidict):
    if start >= numbers_length:
        return 0
    result = pidict[start]
    if result != -1:
        return result
    result = float('inf')
    for i in range(3, 6):
        result = pidict[start+i] = min(result, memorize(start+i, numbers, numbers_length, pidict) + classify(start, start+i-1, numbers))
    return result


def pi():
    total_tests = int(readline())
    for testcase in range(total_tests):
        numbers = readline()
        numbers_length = len(numbers)
        pidict = defaultdict(lambda:-1)
        print memorize(0, numbers, numbers_length, pidict)


if __name__ == '__main__':
    pi()  # run
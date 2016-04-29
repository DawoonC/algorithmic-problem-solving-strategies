# Problem ID: TRIPATHCNT
# https://algospot.com/judge/problem/read/TRIPATHCNT
# 297ms

from collections import defaultdict

def readline():
    return raw_input()


def find_biggest_path(y, x, height, triangle, tridict):
    if y == height-1:
        return triangle[y][x]
    result = tridict[(y,x)]
    if result != -1:
        return result
    result = tridict[(y,x)] = max(find_biggest_path(y+1, x, height, triangle, tridict), find_biggest_path(y+1, x+1, height, triangle, tridict)) + triangle[y][x]
    return result


def get_path_count(y, x, height, triangle, tridict, countdict):
    if y == height-1:
        return 1
    result = countdict[(y,x)]
    if result != -1:
        return result
    result = 0
    if find_biggest_path(y+1, x+1, height, triangle, tridict) >= find_biggest_path(y+1, x, height, triangle, tridict):
        result += get_path_count(y+1, x+1, height, triangle, tridict, countdict)
        countdict[(y,x)] = result;
    if find_biggest_path(y+1, x+1, height, triangle, tridict) <= find_biggest_path(y+1, x, height, triangle, tridict):
        result += get_path_count(y+1, x, height, triangle, tridict, countdict)
        countdict[(y,x)] = result;
    return result


def tripathcnt():
    total_tests = int(readline())
    for testcase in range(total_tests):
        height = int(readline())
        triangle = []
        for i in range(height):
            triangle.append(map(int, readline().split()))
        countdict = defaultdict(lambda:-1)
        tridict = defaultdict(lambda:-1)
        print get_path_count(0, 0, height, triangle, tridict, countdict)


if __name__ == '__main__':
    tripathcnt()  # run
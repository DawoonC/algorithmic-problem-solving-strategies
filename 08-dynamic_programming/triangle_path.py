# Problem ID: TRIANGLEPATH
# https://algospot.com/judge/problem/read/TRIANGLEPATH
# took 258ms

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


def triangle_path():
    total_tests = int(readline())
    for testcase in range(total_tests):
        height = int(readline())
        triangle = []
        for i in range(height):
            triangle.append(map(int, readline().split()))
        countdict = defaultdict(lambda:-1)
        tridict = defaultdict(lambda:-1)
        print find_biggest_path(0, 0, height, triangle, tridict)


if __name__ == '__main__':
    triangle_path()  # run
# coding=utf-8
# Problem ID: NERD2
# https://algospot.com/judge/problem/read/NERD2


def is_dominated(coords, x, y, count):

    for key in coords.keys():
        if x < key:
            if y < coords[key]:
                del coords[x]
            else:
                break

    for key in coords.keys():
        if x > key:
            if y > coords[key]:
                del coords[key]
            else:
                break

    print coords
    return len(coords.keys())


def runner():
    total_tests = int(raw_input())
    for testcase in range(total_tests):
        number = int(raw_input())
        coords = {}
        count = 0
        for i in range(number):
            x, y = map(int, raw_input().split())
            coords[x] = y
            count += is_dominated(coords, x, y, count)
        print count

runner()

'''
2
4
72 50
57 67
74 55
64 60
5
1 5
2 4
3 3
4 2
5 1
'''
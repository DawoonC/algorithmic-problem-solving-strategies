# coding=utf-8
# Problem ID: NUMB3RS
# https://algospot.com/judge/problem/read/NUMB3RS

from collections import defaultdict

def search(current, today, destination, num_of_vil, d_day, matrix, cache):
    if today == d_day:
        return 1.0 if current == destination else 0.0
    result = cache[(current,today)]
    if result > -0.5:
        return result
    result = 0.0
    degree = float(matrix[current].count(1))
    for i in range(num_of_vil):
        if matrix[current][i] == 1:
            result += search(i, today+1, destination, num_of_vil, d_day, matrix, cache) / degree
    cache[(current,today)] = result
    return result


def reverse_search(current, today, prison, num_of_vil, matrix, cache):
    if today == 0:
        return 1.0 if current == prison else 0.0
    result = cache[(current,today)]
    if result > -0.5:
        return result
    result = 0.0
    for i in range(num_of_vil):
        degree = float(matrix[i].count(1))
        if matrix[current][i] == 1:
            result += reverse_search(i, today-1, prison, num_of_vil, matrix, cache) / degree
    cache[(current,today)] = result
    return result


def numb3rs():
    total_tests = int(raw_input())
    for testcase in range(total_tests):
        num_of_vil, d_day, prison = map(int, raw_input().split())
        matrix = []
        for i in range(num_of_vil):
            matrix.append(map(int, raw_input().split()))
        num_of_destination = int(raw_input())
        destination_list = map(int, raw_input().split())
        result = []
        cache = defaultdict(lambda:-1.0)
        for destination in destination_list:
            # cache = defaultdict(lambda:-1.0)
            # result.append(search(prison, 0, destination, num_of_vil, d_day, matrix, cache))
            result.append(reverse_search(destination, d_day, prison, num_of_vil, matrix, cache))
        print ' '.join(map(str, result))


numb3rs()

'''
2
5 2 0
0 1 1 1 0
1 0 0 0 1
1 0 0 0 0
1 0 0 0 0
0 1 0 0 0
3
0 2 4
8 2 3
0 1 1 1 0 0 0 0
1 0 0 1 0 0 0 0
1 0 0 1 0 0 0 0
1 1 1 0 1 1 0 0
0 0 0 1 0 0 1 1
0 0 0 1 0 0 0 1
0 0 0 0 1 0 0 0
0 0 0 0 1 1 0 0
4
3 1 2 6
'''
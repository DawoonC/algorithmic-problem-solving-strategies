# coding=utf-8
# Problem ID: NUMB3RS
# https://algospot.com/judge/problem/read/NUMB3RS

from collections import defaultdict
MOD = 10*1000*1000

def deg():
    pass

def search(path, d, q):
    pass


def runner():
    total_tests = int(raw_input())
    for testcase in range(total_tests):
        n, d, p = map(int, raw_input().split())
        path = []
        for i in range(n):
            path.append([int(x) for x in raw_input().split()])
        t = int(raw_input())
        q = [int(x) for x in raw_input().split()]
        cache = defaultdict(lambda:-1)



runner()
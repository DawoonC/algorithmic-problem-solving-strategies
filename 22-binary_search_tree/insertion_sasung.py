# coding=utf-8
# Problem ID: INSERTION
# https://algospot.com/judge/problem/read/INSERTION

def insertion(a, m):
    for i in range(len(m)-1, 0, -1):
        print "first",i+1, a[i-m[i]], a
        a.insert(i+1, a[i-m[i]])
        print "second",a
        del a[i-m[i]]
    return ' '.join([str(x) for x in a])

def runner():
    total_tests = int(raw_input())
    for testcase in range(total_tests):
        n = int(raw_input())
        m = [int(x) for x in raw_input().split()]
        a = range(1, n+1)
        print insertion(a, m)

runner()

'''
2
5
0 1 1 2 3
4
0 1 2 3
'''
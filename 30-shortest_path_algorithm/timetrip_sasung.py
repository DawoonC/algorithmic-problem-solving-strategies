# Problem ID: TIMETRIP
# https://algospot.com/judge/problem/read/TIMETRIP

import sys


def solve(g, w, e, reachable):
    dist = [sys.maxint] * g

    dist[0] = 0
    for k in xrange(g-1):
        for here in xrange(g):
            for there, cost in e[here]:
                if dist[there] > dist[here] + cost:
                    dist[there] = dist[here] + cost

    for here in xrange(g):
        for there, cost in e[here]:
            if dist[there] > dist[here] + cost:
                if reachable[0][here] and reachable[here][1]:
                    return sys.maxint

    return dist[1]



def runner():

    for i in xrange(int(raw_input())):
        g, w = map(int, raw_input().split())
        e = [[]  for _ in xrange(g)]
        e_neg = [[] for _ in xrange(g)]
        reachable = [[False] * g for _ in xrange(g)]
        for i in xrange(g):
            reachable[i][i] = True


        for _ in xrange(w):
            i, j, value = map(int, raw_input().split())
            e[i].append((j,value))
            e_neg[i].append((j,-value))
            reachable[i][j] = True


        for k in xrange(g):
            for i in xrange(g):
                for j in xrange(g):
                    reachable[i][j] = reachable[i][j] or (reachable[i][k] and reachable[k][j])

        # print reachable

        if not reachable[0][1] :
            print 'UNREACHABLE'
            continue


        ret1 = solve(g,w,e,reachable)
        ret2 = -solve(g,w,e_neg,reachable)
        max_value = 10**10
        if ret1 > max_value:
            ret1 = 'INFINITY'
        if abs(ret2) > max_value:
            ret2 = 'INFINITY'

        print ret1, ret2


runner()

# reachable = [[False] * 5 for _ in xrange(5)]
# print reachable


'''
4
2 2
0 1 1
0 1 3
4 4
0 2 -7
0 3 -4
3 2 9
2 1 3
4 3
0 2 0
2 2 1
2 1 0
3 0
'''
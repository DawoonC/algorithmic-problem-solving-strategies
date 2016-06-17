# Problem ID: DICTIONARY
# https://algospot.com/judge/problem/read/DICTIONARY

eng = lambda x:ord(x)-ord('a')

def make_graph(i, j, adj):
    for k in xrange(min(len(i),len(j))):
        x,y = i[k],j[k]
        if x!=y:
            adj[eng(x)][eng(y)] = 1
            break

def dfs(i, adj, vertex, order):
    vertex[i] = 1
    for j in xrange(26):
        if adj[i][j] == 1 and vertex[j] == 0:
            dfs(j, adj, vertex, order)
    order.append(i)

def runner():
    total_tests = input()
    for testcase in xrange(total_tests):
        n = input()
        words = [raw_input() for i in xrange(n)]
        adj = [[0]*26 for i in xrange(26)]
        vertex = [0] * 26
        order = []
        error = 0

        for i in xrange(n-1):
            make_graph(words[i], words[i+1],adj)

        for i in xrange(26):
            if vertex[i] == 0:
                dfs(i, adj, vertex, order)

        # print adj
        # print order
        order.reverse()
        for i in xrange(26):
            for j in xrange(i+1, 26):
                if adj[order[j]][order[i]]:
                    error = 1
                    break

        if error==1:
            print 'INVALID HYPOTHESIS'
        else:
            print ''.join(str(chr(i+97)) for i in order)

runner()

'''
3
3
ba
aa
ab
5
gg
kia
lotte
lg
hanhwa
6
dictionary
english
is
ordered
ordinary
this
'''
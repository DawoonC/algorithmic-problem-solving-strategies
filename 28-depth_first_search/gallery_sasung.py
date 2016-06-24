# Problem ID: GALLERY
# https://algospot.com/judge/problem/read/GALLERY
# 313ms

from collections import defaultdict

def dfs(now):
    global installed
    visited[now] = 1
    children = {'watched': 0, 'unwatched': 0, 'installed': 0}
    for nxt in halls[now]:
        if not visited[nxt]:
            children[dfs(nxt)] += 1
    if children['unwatched']:
        installed += 1
        return 'installed'
    if children['installed']:
        return 'watched'
    return 'unwatched'


for case in range(int(input())):
    G, H = map(int, raw_input().split())
    halls = defaultdict(list)
    visited = [0] * G
    installed = 0

    for a, b in (map(int, raw_input().split()) for _ in range(H)):
        halls[a].append(b)
        halls[b].append(a)
    print halls

    for i in range(G):
        if not visited[i] and dfs(i) == 'unwatched':
            installed += 1

    print(installed)


'''
3
6 5
0 1
1 2
1 3
2 5
0 4
4 2
0 1
2 3
1000 1
0 1

'''
# Problem ID: LAN
# https://algospot.com/judge/problem/read/LAN
# took > 1000ms

from math import sqrt
import heapq


def readline():
    return raw_input()


def get_distance(a, b, x_list, y_list):
    return sqrt(((y_list[a] - y_list[b]) ** 2) + ((x_list[a] - x_list[b]) ** 2))


def lan_prim(root, pre_connected, n, x_list, y_list):
    queue = [(0, root)]
    visited = set()
    total = 0
    while queue:
        w, curr = heapq.heappop(queue)
        if curr in visited:
            continue
        total += w
        visited.add(curr)
        for neighbor in xrange(n):
            if curr != neighbor and neighbor not in visited:
                new_w = 0
                if (curr, neighbor) not in pre_connected:
                    new_w = get_distance(curr, neighbor, x_list, y_list)
                heapq.heappush(queue, (new_w, neighbor))
    return total


def lan():
    total_tests = int(readline())
    for _ in xrange(total_tests):
        n_v, n_exist = map(int, readline().split())
        x_list = map(int, readline().split())
        y_list = map(int, readline().split())
        pre_connected = set()
        for _ in xrange(n_exist):
            u, v = map(int, readline().split())
            pre_connected.add((u, v))
            pre_connected.add((v, u))
        result = lan_prim(0, pre_connected, n_v, x_list, y_list)
        print '%.10f' % result


if __name__ == '__main__':
    lan()  # run

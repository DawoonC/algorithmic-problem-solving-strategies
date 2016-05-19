# coding=utf-8
# Problem ID: FORTRESS
# https://algospot.com/judge/problem/read/FORTRESS
'''
2
3
5 5 15
5 5 10
5 5 5
8
21 15 20
15 15 10
13 12 5
12 12 3
19 19 2
30 24 5
32 10 7
32 9 4
'''


class Tree(object):
    def __init__(self):
        self.child = []

def sqr(x):
    return x * x

def sqr_dist(a, b, x, y, r):
    return sqr(y[a] - y[b]) + sqr(x[a] - x[b])

def encloses(a, b, x, y, r):
    if (r[a] > r[b] and sqr_dist(a,b, x, y, r) < sqr(r[a] - r[b])):
        return True
    else:
        return False

def is_child(parent, child, fortress_number, x, y, r):
    if encloses(parent, child, x, y, r) == False:
        return False

    for i in range(fortress_number):
        if(i != parent and i != child and encloses(parent,i, x, y, r) and encloses(i, child, x, y, r)):
            return False

    return True

def get_tree(root, fortress_number, x, y, r):
    ret = Tree()
    for i in range(fortress_number):
        if is_child(root, i, fortress_number, x, y, r):
            ret.child.append(get_tree(i, fortress_number, x, y, r))
    return ret


def height(root, longest):
    heights = []
    for i in range(len(root.child)):
        heights.append(height(root.child[i], longest))
    if len(heights) == 0:
        return 0
    heights.sort()
    if len(heights) > 1:
        # print heights
        longest[0] = max(longest[0], 2 + heights[-2] + heights[-1])
        # print(longest)
    return heights[-1] + 1


def solve(root):
    longest = [0]
    h = height(root, longest)
    # print h, longest
    return max(longest[0], h)

def runner():
    total_tests = int(raw_input())
    for testcase in range(total_tests):
        fortress_number = int(raw_input())
        x = []
        y = []
        r = []
        for i in range(fortress_number):
            a, b, c = map(int, raw_input().split())
            x.append(a)
            y.append(b)
            r.append(c)
        root = get_tree(0, fortress_number, x, y, r)
        print solve(root)

runner()

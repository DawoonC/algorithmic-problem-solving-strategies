# Problem ID: FORTRESS
# https://algospot.com/judge/problem/read/FORTRESS
# timeout

from collections import defaultdict

class Wall(object):
    def __init__(self):
        self.child = []


def readline():
    return raw_input()


def sqrdist(a, b, x_list, y_list):
    return ((y_list[a] - y_list[b])**2) + ((x_list[a] - x_list[b])**2)


def encloses(a, b, x_list, y_list, r_list):
    return r_list[a] > r_list[b] and sqrdist(a, b, x_list, y_list) < (r_list[a] - r_list[b])**2


def is_child(parent, child, x_list, y_list, r_list, n, child_dict):
    if child_dict[(parent,child)] != None:
        return child_dict[(parent,child)]
    result = None
    if not encloses(parent, child, x_list, y_list, r_list):
        result = child_dict[(parent,child)] = False
        return result
    for i in range(n):
        if i != parent and i != child and encloses(parent, i, x_list, y_list, r_list) and encloses(i, child, x_list, y_list, r_list):
            result = child_dict[(parent,child)] = False
            return result
    result = child_dict[(parent,child)] = True
    return result


def get_tree(root, x_list, y_list, r_list, n, child_dict):
    tree = Wall()
    for node in range(n):
        if is_child(root, node, x_list, y_list, r_list, n, child_dict):
            tree.child.append(get_tree(node, x_list, y_list, r_list, n, child_dict))
    return tree


def find_height(root_node, longest):
    heights = []
    for i in range(len(root_node.child)):
        heights.append(find_height(root_node.child[i], longest))
    if len(heights) == 0:
        return 0
    heights.sort()
    if len(heights) > 1:
        longest[0] = max(longest[0], 2 + heights[-2] + heights[-1])
    return heights[-1] + 1


def find_longest_path(root_node):
    longest = [0]
    height = find_height(root_node, longest)
    return max(longest[0], height)


def fortress():
    total_tests = int(readline())
    for testcase in range(total_tests):
        n = int(readline())
        x_list, y_list, r_list = [], [], []
        child_dict = defaultdict(lambda: None)
        for i in range(n):
            x, y, r = map(int, readline().split())
            x_list.append(x)
            y_list.append(y)
            r_list.append(r)
        root_node = get_tree(0, x_list, y_list, r_list, n, child_dict)
        print find_longest_path(root_node)


if __name__ == '__main__':
    fortress()  # run

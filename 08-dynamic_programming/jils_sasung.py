from collections import defaultdict

def get_jlis(index_a, index_b, a_list, b_list, cache):
    # print(cache)
    ret = cache[(index_a + 1, index_b + 1)]
    if ret != -1:
        return ret

    ret = 2
    if index_a == -1:
        a = -100
    else:
        a = a_list[index_a]
    if index_b == -1:
        b = -100
    else:
        b = b_list[index_b]

    max_element = max(a, b)
    # print index_a, index_b

    for i in range(index_a + 1, len(a_list)):
        if max_element < a_list[i]:
            # print i, index_b
            ret = cache[(i, index_b)] = max(ret, get_jlis(i, index_b, a_list, b_list, cache) + 1)
            # print i, index_b, cache[i, index_b], cache

    for j in range(index_b + 1, len(b_list)):
        if max_element < b_list[j]:
            ret = cache[(index_a, j)] = max(ret, get_jlis(index_a, j, a_list, b_list, cache) + 1)

    return ret

def jlis():
    total_tests = int(raw_input())
    for testcase in range(total_tests):
        a_length, b_length = map(int, raw_input().split())
        a_list = map(int, raw_input().split())
        b_list = map(int, raw_input().split())
        cache = defaultdict(lambda:-1)
        print get_jlis(-1, -1, a_list, b_list, cache) - 2

jlis()

'''
3
3 3
1 2 4
3 4 7
3 3
1 2 3
4 5 6
5 3
10 20 30 1 2
10 20 30
'''
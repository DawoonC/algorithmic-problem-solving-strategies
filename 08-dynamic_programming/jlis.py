# Problem ID: JLIS
# https://algospot.com/judge/problem/read/JLIS
# timeout

from collections import defaultdict

def readline():
    return raw_input()


def get_jlis_length(i, j, a_list, b_list, a_length, b_length, jlisdict):
    result = jlisdict[(i+1,j+1)]
    if result != -1:
        return result
    result = 2
    a_val = -10 if i == -1 else a_list[i]
    b_val = -10 if j == -1 else b_list[j]
    max_val = max(a_val, b_val)
    for k in range(i+1, a_length):
        if max_val < a_list[k]:
            result = jlisdict[(k,j)] = max(result, get_jlis_length(k, j, a_list, b_list, a_length, b_length, jlisdict) + 1)
    for l in range(j+1, b_length):
        if max_val < b_list[l]:
            result = jlisdict[(i,l)] = max(result, get_jlis_length(i, l, a_list, b_list, a_length, b_length, jlisdict) + 1)
    return result


def jlis():
    total_tests = int(readline())
    for testcase in range(total_tests):
        a_length, b_length = map(int, readline().split())
        a_list = map(int, readline().split())
        b_list = map(int, readline().split())
        jlisdict = defaultdict(lambda:-1)
        print get_jlis_length(-1, -1, a_list, b_list, a_length, b_length, jlisdict) - 2


if __name__ == '__main__':
    jlis()  # run
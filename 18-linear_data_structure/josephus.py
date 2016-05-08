# Problem ID: JOSEPHUS
# https://algospot.com/judge/problem/read/JOSEPHUS
# 56ms for non-recursive solution
# recursion depth error for recursive solution

def readline():
    return raw_input()


def find_last_two(n_list, k, next_die):
    n_list.pop(next_die)
    n_list_len = len(n_list)
    if n_list_len == 2:
        return ' '.join(map(str, n_list))
    next_die = next_die + k - 1
    next_die = next_die % n_list_len if next_die >= n_list_len else next_die
    return find_last_two(n_list, k, next_die)


# non-recursive solution
def find_last_two_iter(n_list, k, next_die):
    n_list.pop(next_die)
    n_list_len = len(n_list)
    while n_list_len > 2:
        next_die = next_die + k - 1
        next_die = next_die % n_list_len if next_die >= n_list_len else next_die
        n_list.pop(next_die)
        n_list_len = len(n_list)
    return ' '.join(map(str, n_list))


def josephus():
    total_tests = int(readline())
    for testcase in range(total_tests):
        n, k = map(int, readline().split())
        n_list = range(1, n+1)
        print find_last_two_iter(n_list, k, 0)


if __name__ == '__main__':
    josephus()  # run
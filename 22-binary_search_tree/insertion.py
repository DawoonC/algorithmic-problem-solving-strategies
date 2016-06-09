# Problem ID: INSERTION
# https://algospot.com/judge/problem/read/INSERTION
# timeout

from treap import TreapNode

def readline():
    return raw_input()


def reverse_insert_sort(n, shifted, result):
    candidates = None
    for i in range(n):
        if candidates is None: candidates = TreapNode(i+1)
        else:
            candidates = candidates.insert(TreapNode(i+1))
    for i in range(n-1, -1, -1):
        larger = shifted[i]
        kth = candidates.get_kth(i + 1 - int(larger))
        result[i] = kth.key
        candidates = candidates.erase(kth.key)


def insertion():
    total_tests = int(readline())
    for testcase in range(total_tests):
        n = int(readline())
        result = [None] * n
        shifted = readline().split()
        reverse_insert_sort(n, shifted, result)
        print ' '.join(result)


if __name__ == '__main__':
    insertion()  # run

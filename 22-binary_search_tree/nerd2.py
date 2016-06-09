# Problem ID: NERD2
# https://algospot.com/judge/problem/read/NERD2
# timeout

import heapq

def readline():
    return raw_input()


class Applicant(object):
    def __init__(self, counts):
        self.pr_cnt = counts[0]
        self.rm_cnt = counts[1]
        self.total = sum(counts)
    #
    def __cmp__(self, other):
        if self.pr_cnt < other.pr_cnt and self.rm_cnt < other.rm_cnt:
            return -1
        else:
            return cmp(self.total, other.total)


def check_nerdiness(new_comer, nerd_list, result_tracker, i):
    if i == 0:
        heapq.heappush(nerd_list, Applicant(new_comer))
        result_tracker['current_len'] += 1
    if new_comer[0] > nerd_list[0].pr_cnt or new_comer[1] > nerd_list[0].rm_cnt:
        heapq.heappush(nerd_list, Applicant(new_comer))
        result_tracker['current_len'] += 1
    while new_comer[0] > nerd_list[0].pr_cnt and new_comer[1] > nerd_list[0].rm_cnt:
        heapq.heappop(nerd_list)
        result_tracker['current_len'] -= 1
    result_tracker['sum'] += result_tracker['current_len']


def nerd2():
    total_tests = int(readline())
    for testcase in range(total_tests):
        n = int(readline())
        nerd_list = []
        result_tracker = {
            'current_len': 0,
            'sum': 0
        }
        for i in range(n):
            new_comer = map(int, readline().split())
            check_nerdiness(new_comer, nerd_list, result_tracker, i)
        print result_tracker['sum']


if __name__ == '__main__':
    nerd2()  # run

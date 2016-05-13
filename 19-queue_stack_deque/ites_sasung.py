# coding=utf-8
# Problem ID: ITES
# https://algospot.com/judge/problem/read/ITES

def ites(k,n):

    input_queue = [1983]
    signal_queue = [1983]
    count = 0
    range_sum = sum(signal_queue)
    if range_sum == k:
        count += 1
    for i in range(1, n):
        input_queue.append((input_queue[-1] * 214013 + 2531011) % pow(2,32))
        # print input_queue
        input_queue.pop(0)
        signal_queue.append(input_queue[-1] % 10000 + 1)
        # print signal_queue
        range_sum += signal_queue[-1]
        if range_sum == k:
            count += 1
        while range_sum > k:
            range_sum -= signal_queue.pop(0)
            if range_sum == k:
                count += 1
    return count


def runner():
    total_tests = int(raw_input())
    for testcase in range(total_tests):
        k, n = map(int, raw_input().split())
        print ites(k,n)

runner()



# Problem ID: ITES
# https://algospot.com/judge/problem/read/ITES

def readline():
    return raw_input()


def count_k(k, n):
    input_queue = [1983]
    signal_queue = [1984]
    count = 0
    _2_32 = 2**32
    subsum = sum(signal_queue)
    if subsum == k:
        count += 1
    for i in range(1, n):
        input_queue.append((input_queue[-1] * 214013 + 2531011) % _2_32)
        input_queue.pop(0)
        signal_queue.append(input_queue[-1] % 10000 + 1)
        subsum += signal_queue[-1]
        if subsum == k:
            count += 1
        while subsum > k:
            subsum -= signal_queue.pop(0)
            if subsum == k:
                count += 1
    return count


def ites():
    total_tests = int(readline())
    for testcase in range(total_tests):
        k, n = map(int, readline().split())
        print count_k(k, n)


if __name__ == '__main__':
    ites()  # run

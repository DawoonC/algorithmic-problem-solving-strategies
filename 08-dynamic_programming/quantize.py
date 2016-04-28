# Problem ID: QUANTIZE
# https://algospot.com/judge/problem/read/QUANTIZE
# took 1250ms

from collections import defaultdict

def readline():
    return raw_input()


def precalc(numbers, num_length, sum_dict, sq_sum_dict):
    sum_dict[0] = numbers[0]
    sq_sum_dict[0] = numbers[0] ** 2
    for i in range(1, num_length):
        sum_dict[i] = sum_dict[i-1] + numbers[i]
        sq_sum_dict[i] = sq_sum_dict[i-1] + (numbers[i] ** 2)


def min_error(low, high, sum_dict, sq_sum_dict):
    sub_sum = sum_dict[high] - (0 if low == 0 else sum_dict[low-1])
    sub_sq_sum = sq_sum_dict[high] - (0 if low == 0 else sq_sum_dict[low-1])
    mean = int(0.5 + (sub_sum / (high - low + 1.0)))
    result = sub_sq_sum - (2 * mean * sub_sum) + (mean ** 2 * (high - low + 1))
    return result


def get_quantized(_from, parts, num_length, q_dict, sum_dict, sq_sum_dict):
    if _from == num_length:
        return 0
    if parts == 0:
        return float('inf')
    result = q_dict[(_from,parts)]
    if result != -1:
        return result
    result = float('inf')
    for part_size in range(1, num_length-_from+1):
        result = q_dict[(_from,parts)] = min(result, min_error(_from, _from+part_size-1, sum_dict, sq_sum_dict) + 
                                                     get_quantized(_from+part_size, parts-1, num_length, q_dict, sum_dict, sq_sum_dict))
    return result


def quantize():
    total_tests = int(readline())
    for testcase in range(total_tests):
        num_length, q_length = map(int, readline().split())
        numbers = sorted(map(int, readline().split()))
        sum_dict = defaultdict(int)
        sq_sum_dict = defaultdict(int)
        q_dict = defaultdict(lambda:-1)
        precalc(numbers, num_length, sum_dict, sq_sum_dict)
        print get_quantized(0, q_length, num_length, q_dict, sum_dict, sq_sum_dict)



if __name__ == '__main__':
    quantize()  # run
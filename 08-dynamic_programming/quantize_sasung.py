# coding=utf-8
# Problem ID: QUANTIZE
# https://algospot.com/judge/problem/read/QUANTIZE

from collections import defaultdict

inf = 987654321


#p_sum은 A의 부분 합 미리 저장, p_sq_sum은 A 제곱의 부분합 미리 저장
def pre_calc(A, p_sum, p_sq_sum, total_length):
    A.sort()
    p_sum.append(A[0])
    p_sq_sum.append(A[0] * A[0])

    for i in range(1, total_length):
        p_sum.append(p_sum[i-1] + A[i])
        p_sq_sum.append(p_sq_sum[i-1] + A[i] * A[i])


#lo번째 숫자부터 hi번재 숫자까지 하나의 수로 표현했을 때의 최소 오류 반환
def min_error(lo, hi, p_sum, p_sq_sum):
    if lo == 0:
        sum = p_sum[hi] - 0
        sq_sum = p_sq_sum[hi] - 0
    else:
        sum = p_sum[hi] - p_sum[lo-1]
        sq_sum = p_sq_sum[hi] - p_sq_sum[lo-1]

    m = round(float(sum) / (hi-lo+1))
    ret = int(sq_sum - (2 * m * sum) + (m * m * (hi-lo+1)))
    return ret


def quantize(prev, total_length, parts, cache, p_sum, p_sq_sum):
    #기저 사례 : 모든 숫자 다 양자화했을 때
    if prev == total_length:
        return 0

    #기저 사례 :  묶을 수 있는 숫자를 다 사용함, 큰 값을 반환
    if parts == 0:
        return inf

    #캐시 가져오기
    ret = cache[prev, parts]

    #캐시에 있으면 반환
    if ret != -1:
        return ret

    ret = inf

    for part_size in range(1 , total_length - prev + 1):
        ret = cache[prev, parts] = min(ret, min_error(prev, prev + part_size - 1, p_sum, p_sq_sum) + quantize(prev + part_size, total_length, parts -1, cache, p_sum, p_sq_sum))

    return ret


def runner():
    total_tests = int(raw_input())
    for testcase in range(total_tests):
        total_length, parts = map(int, raw_input().split())
        A = [int(x) for x in raw_input().split()]
        cache = defaultdict(lambda:-1)
        p_sum = []
        p_sq_sum = []
        pre_calc(A, p_sum, p_sq_sum, total_length)
        print quantize(0, total_length, parts, cache, p_sum, p_sq_sum)


runner()

# 2
# 10 3
# 3 3 3 1 2 3 2 2 2 1
# 9 3
# 1 744 755 4 897 902 890 6 777
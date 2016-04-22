# coding=utf-8
# https://algospot.com/judge/problem/read/FENCE

def solve(fence_height, left, right):
    if left == right:
        return fence_height[left]

    mid = (left + right) / 2
    ret = max(solve(fence_height, left, mid), solve(fence_height, mid + 1, right))
    # print ret
    lo = mid
    hi = mid + 1
    height = min(fence_height[lo], fence_height[hi])
    print height
    ret = max(ret, height * 2)

    while left < lo or hi < right:
        if hi < right and (lo == left or fence_height[lo - 1] < fence_height[hi + 1]):
            hi += 1
            height = min(height, fence_height[hi])
        else:
            lo -= 1
            height = min(height, fence_height[lo])

        ret = max(ret, height * (hi - lo + 1))

    return ret


a = [7, 1, 5, 9, 6, 7, 3]
print(solve(a, 0, 6))

def fence():
    total_tests = int(raw_input())
    for testcase in range(total_tests):
        total_fence = int(raw_input())
        fence_height = [int(x) for x in raw_input().split()]
        print(solve(fence_height, 0, total_fence-1))

# fence()
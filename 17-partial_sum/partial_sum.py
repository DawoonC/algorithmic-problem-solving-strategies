def partial_sum(nums):
    psum = nums[:]
    for i in range(1, len(psum)):
        psum[i] = psum[i - 1] + psum[i]
    return psum


def range_sum(psum, a, b):
    if a == 0:
        return psum[b]
    return psum[b] - psum[a - 1]

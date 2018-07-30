# A sequence X_1, X_2, ..., X_n is fibonacci-like if:
# - n >= 3
# - X_i + X_{i+1} = X_{i+2} for all i + 2 <= n
#
# Given a strictly increasing array `nums` of positive integers forming a sequence,
# find the length of the longest fibonacci-like subsequence of `nums`. If one does not exist, return 0.
#
# (Recall that a subsequence is derived from another sequence `nums`
# by deleting any number of elements (including none) from `nums`,
# without changing the order of the remaining elements.
# For example, [3, 5, 8] is a subsequence of [3, 4, 5, 6, 7, 8].)

from collections import defaultdict


# brute force way (O(n^2 log m))
def len_of_longest_fib_subseq(nums):
    num_set = set(nums)
    n = len(nums)
    result = 0
    for i in xrange(n):
        for j in xrange(i + 1, n):
            x, y = nums[j], nums[i] + nums[j]
            length = 2
            while y in num_set:
                x, y = y, x + y
                length += 1
            result = max(result, length)
    if result < 3:
        return 0
    return result


# with dynamic programming (O(n^2))
def len_of_longest_fib_subseq_dp(nums):
    num_map = {x: i for i, x in enumerate(nums)}
    cache = defaultdict(lambda: 2)
    result = 0
    # nums[k] = nums[i] + nums[j]
    for k, x in enumerate(nums):
        for j in xrange(k):
            i = num_map.get(x - nums[j], None)
            if i is not None and i < j:
                candidate = cache[(j, k)] = cache[(i, j)] + 1
                result = max(result, candidate)
    if result < 3:
        return 0
    return result


def test():
    # Input: [1,2,3,4,5,6,7,8]
    # Output: 5
    # Explanation:
    # The longest subsequence that is fibonacci-like: [1,2,3,5,8].
    a = [1,2,3,4,5,6,7,8]
    result = len_of_longest_fib_subseq_dp(a)
    assert result == 5
    # Input: [1,3,7,11,12,14,18]
    # Output: 3
    # Explanation:
    # The longest subsequence that is fibonacci-like:
    # [1,11,12], [3,11,14] or [7,11,18].
    a = [1,3,7,11,12,14,18]
    result = len_of_longest_fib_subseq_dp(a)
    assert result == 3
    print 'test success!'


if __name__ == '__main__':
    test()  # run

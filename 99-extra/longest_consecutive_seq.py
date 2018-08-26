# Given an unsorted array of integers,
# find the length of the longest consecutive elements sequence.
# Your algorithm should run in O(n) complexity.
#
# Example:
# Input: [100, 4, 200, 1, 3, 2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.


def longest_consecutive_seq(nums):
    n_set = set(nums)
    result = 0
    for e in nums:
        if e - 1 not in n_set:
            curr = e
            cand = 1
            while curr + 1 in n_set:
                cand += 1
                curr += 1
            result = max(result, cand)
    return result


def test():
    # Input: [100, 4, 200, 1, 3, 2]
    # Output: 4
    nums = [100, 4, 200, 1, 3, 2]
    expected = 4
    result = longest_consecutive_seq(nums)
    assert result == expected
    print 'test success!'


if __name__ == '__main__':
    test()  # run

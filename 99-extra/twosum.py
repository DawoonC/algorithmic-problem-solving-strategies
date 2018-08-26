# Given an array of integers, return indices of the two numbers
# such that they add up to a specific target.
# return None if not exist.


def twosum(nums, target):
    memo = {}
    for i in xrange(len(nums)):
        cand = target - nums[i]
        if cand in memo:
            return [memo[cand], i]
        memo[nums[i]] = i
    return None


def test():
    # Input: nums = [2, 7, 11, 15], target = 9
    # Output: [0, 1]
    nums = [2, 7, 11, 15]
    target = 9
    expected = [0, 1]
    result = twosum(nums, target)
    assert result == expected
    # Input: nums = [2, 7, 11, 15], target = 17
    # Output: [0, 3]
    target = 17
    expected = [0, 3]
    result = twosum(nums, target)
    assert result == expected
    # Input: nums = [2, 7, 11, 15], target = 20
    # Output: None
    target = 20
    expected = None
    result = twosum(nums, target)
    assert result == expected
    print 'test success!'


if __name__ == '__main__':
    test()  # run

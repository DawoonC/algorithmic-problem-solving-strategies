def max_subarray(nums):
    max_sum = -float('inf')
    curr_sum = -float('inf')
    for e in nums:
        curr_sum = max(e, curr_sum + e)
        max_sum = max(max_sum, curr_sum)
    return max_sum


def test():
    # Input: [-2,1,-3,4,-1,2,1,-5,4]
    # Output: 6
    # Explanation: [4,-1,2,1] has the largest sum = 6.
    a = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    result = max_subarray(a)
    assert result == 6
    a = [31, -41, 59, 26, -53, 58, 97, -93, -23, 84]
    result = max_subarray(a)
    assert result == 187
    print 'test success!'


if __name__ == '__main__':
    test()  # run

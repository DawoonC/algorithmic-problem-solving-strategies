def max_product_subarray(nums):
    max_p = nums[0]
    min_p = nums[0]
    result = nums[0]
    for i in xrange(1, len(nums)):
        if nums[i] < 0:
            max_p, min_p = min_p, max_p
        max_p = max(nums[i], max_p * nums[i])
        min_p = min(nums[i], min_p * nums[i])
        result = max(result, max_p)
    return result


def test():
    # Input: [2,3,-2,4]
    # Output: 6
    # Explanation: [2,3] has the largest product 6.
    a = [2, 3, -2, 4]
    result = max_product_subarray(a)
    assert result == 6
    # Input: [-2,0,-1]
    # Output: 0
    # Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
    a = [-2, 0, -1]
    result = max_product_subarray(a)
    assert result == 0
    print 'test success!'


if __name__ == '__main__':
    test()  # run

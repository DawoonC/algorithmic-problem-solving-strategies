# Given a sorted integer array without duplicates, return the summary of its ranges.


def summary_ranges(nums):
    result = []
    is_cont = False
    last_cont_i = None
    n = len(nums)
    for i in xrange(n + 1):
        if i == 0:
            last_cont_i = i
            continue
        if i < n and nums[i] - nums[i - 1] == 1:
            is_cont = True
            continue
        if is_cont:
            val = '%s->%s' % (nums[last_cont_i], nums[i - 1])
            result.append(val)
            is_cont = False
            last_cont_i = i
            continue
        result.append(str(nums[last_cont_i]))
        last_cont_i = i
    return result


def test():
    # Input:  [0,1,2,4,5,7]
    # Output: ["0->2","4->5","7"]
    # Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.
    a = [0,1,2,4,5,7]
    result = summary_ranges(a)
    assert result == ["0->2","4->5","7"]
    # Input:  [0,2,3,4,6,8,9]
    # Output: ["0","2->4","6","8->9"]
    # Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.
    a = [0,2,3,4,6,8,9]
    result = summary_ranges(a)
    assert result == ["0","2->4","6","8->9"]
    print 'test success!'


if __name__ == '__main__':
    test()  # run

# Implement next permutation, which rearranges numbers into
# the lexicographically next greater permutation of numbers.
#
# If such arrangement is not possible, it must rearrange it
# as the lowest possible order (ie, sorted in ascending order).
#
# The replacement must be in-place and use only constant extra memory.
#
# Here are some examples. Inputs are in the left-hand column and
# its corresponding outputs are in the right-hand column.
#
# 1,2,3 => 1,3,2
# 3,2,1 => 1,2,3
# 1,1,5 => 1,5,1


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


def next_permutation(nums):
    n = len(nums)
    if n == 0:
        return nums
    found_decreasing = False
    i = n - 2
    while not found_decreasing and i >= 0:
        if nums[i] < nums[i + 1]:
            found_decreasing = True
            break
        i -= 1
    if found_decreasing:
        swap_i = None
        for j in xrange(i + 1, n):
            if nums[j] > nums[i]:
                if swap_i is None:
                    swap_i = j
                    continue
                if nums[j] <= nums[swap_i]:
                    swap_i = j
                    continue
        swap(nums, i, swap_i)
        j, k = i + 1, n - 1
        while j <= k:
            swap(nums, j, k)
            j += 1
            k -= 1
    else:
        nums.reverse()


def test():
    # Input: [1,2,3]
    # Output: [1,3,2]
    nums = [1,2,3]
    expected = [1,3,2]
    next_permutation(nums)
    assert nums == expected
    # Input: [3,2,1]
    # Output: [1,2,3]
    nums = [3,2,1]
    expected = [1,2,3]
    next_permutation(nums)
    assert nums == expected
    # Input: [1,1,5]
    # Output: [1,5,1]
    nums = [1,1,5]
    expected = [1,5,1]
    next_permutation(nums)
    assert nums == expected
    # Input: [3,2,1,3,3]
    # Output: [3,2,3,1,3]
    nums = [3,2,1,3,3]
    expected = [3,2,3,1,3]
    next_permutation(nums)
    assert nums == expected
    print 'test success!'


if __name__ == '__main__':
    test()  # run

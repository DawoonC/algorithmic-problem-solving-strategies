# Write an efficient algorithm that searches for a value in an m x n matrix.
# This matrix has the following properties:
# - Integers in each row are sorted from left to right.
# - The first integer of each row is greater than the last integer of the previous row.


def search_list(lst, target):
    lo, hi = 0, len(lst)
    for _ in xrange(100):
        mid = (lo + hi) / 2
        if lst[mid] > target:
            hi = mid
            continue
        if lst[mid] < target:
            lo = mid
            continue
        if lst[mid] == target:
            return True
    return False


def search_matrix(matrix, target):
    lo, hi = 0, len(matrix)
    if hi == 0 or len(matrix[0]) == 0:
        return False
    for _ in xrange(100):
        mid = (lo + hi) / 2
        if matrix[mid][0] > target:
            hi = mid
            continue
        if matrix[mid][-1] < target:
            lo = mid
            continue
        return search_list(matrix[mid], target)
    return False


def test():
    # Input:
    # matrix = [
    #   [1,   3,  5,  7],
    #   [10, 11, 16, 20],
    #   [23, 30, 34, 50]
    # ]
    # target = 3
    # Output: True
    m = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50],
    ]
    target = 3
    result = search_matrix(m, target)
    assert result is True
    # Input:
    # matrix = [
    #   [1,   3,  5,  7],
    #   [10, 11, 16, 20],
    #   [23, 30, 34, 50]
    # ]
    # target = 13
    # Output: False
    m = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50],
    ]
    target = 13
    result = search_matrix(m, target)
    assert result is False
    print 'test success!'


if __name__ == '__main__':
    test()  # run

# Given a matrix of m x n elements (m rows, n columns),
# return all elements of the matrix in spiral order.


def spiral_matrix(matrix):
    m_rows = len(matrix)
    if m_rows < 1:
        return []
    n_cols = len(matrix[0])
    result = []
    i, j = 0, 0
    direction = 0
    seen = set()
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    for _ in xrange(m_rows * n_cols):
        result.append(matrix[i][j])
        seen.add((i, j))
        cand_i = i + di[direction]
        cand_j = j + dj[direction]
        if (cand_i, cand_j) not in seen and 0 <= cand_i < m_rows and 0 <= cand_j < n_cols:
            i = cand_i
            j = cand_j
        else:
            direction = (direction + 1) % 4
            i = i + di[direction]
            j = j + dj[direction]
    return result


def test():
    # Input:
    # [
    #  [ 1, 2, 3 ],
    #  [ 4, 5, 6 ],
    #  [ 7, 8, 9 ]
    # ]
    # Output: [1,2,3,6,9,8,7,4,5]
    m = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    result = spiral_matrix(m)
    assert result == [1,2,3,6,9,8,7,4,5]
    # Input:
    # [
    #  [1, 2, 3, 4],
    #  [5, 6, 7, 8],
    #  [9,10,11,12]
    # ]
    # Output: [1,2,3,4,8,12,11,10,9,5,6,7]
    m = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9,10,11,12],
    ]
    result = spiral_matrix(m)
    assert result == [1,2,3,4,8,12,11,10,9,5,6,7]
    print 'test success!'


if __name__ == '__main__':
    test()  # run

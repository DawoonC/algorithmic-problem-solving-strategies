# Problem ID: FENCE
# https://algospot.com/judge/problem/read/FENCE

def readline():
    return raw_input()


def solve(fences, left_i, right_i):
    """
    Recursively find widest fence area to preserve.

    Args:
        fences: a list representing each fence board
        left_i: left most index
        right_i: right most index
    Returns:
        widest fence area to preserve
    """
    # base case
    if left_i == right_i:
        return fences[left_i]
    # middle index by split half
    middle_i = (left_i + right_i) / 2
    # get maximum result from both sides
    result = max(solve(fences, left_i, middle_i), solve(fences, middle_i+1, right_i))
    # find area that covers both sides
    m_left_i, m_right_i = middle_i, middle_i+1
    height = min(fences[m_left_i], fences[m_right_i])
    result = max(result, height*2)
    # widen the area from middle
    # always widen to higher side
    while left_i < m_left_i or m_right_i < right_i:
        if m_right_i < right_i and (m_left_i == left_i or fences[m_left_i-1] < fences[m_right_i+1]):
            m_right_i += 1
            height = min(height, fences[m_right_i])
        else:
            m_left_i -= 1
            height = min(height, fences[m_left_i])
        result = max(result, height * (m_right_i - m_left_i + 1))
    return result


def fence():
    total_tests = int(readline())
    for testcase in range(total_tests):
        length = int(readline())
        fences = map(int, readline().split())
        print solve(fences, 0, length-1)


if __name__ == '__main__':
    fence()  # run

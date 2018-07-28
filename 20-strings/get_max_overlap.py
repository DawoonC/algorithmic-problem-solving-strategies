from get_partial_match import get_partial_match


def get_max_overlap(a, b):
    """Finds length of the longest overlap substring between a and b"""
    n, m = len(a), len(b)
    begin, matched = 0, 0
    pi = get_partial_match(b)
    while begin < n:
        if matched < m and a[begin + matched] == b[matched]:
            matched += 1
            if (begin + matched) == n:
                return matched
        else:
            if matched == 0:
                begin += 1
            else:
                begin += (matched - pi[matched - 1])
                matched = pi[matched - 1]
    return 0

from get_partial_match import get_partial_match


def kmp_search(full_str, sub_str):
    """finds all beginning index of sub_str occurred in full_str

    search faster by skipping already known matched positions
    runs in O(n)
    """
    n, m = len(full_str), len(sub_str)
    result = []
    pi = get_partial_match(sub_str)
    begin, matched = 0, 0
    while begin <= (n - m):
        if matched < m and full_str[begin + matched] == sub_str[matched]:
            matched += 1
            if matched == m:
                result.append(begin)
        else:
            if matched == 0:
                begin += 1
            else:
                begin += (matched - pi[matched - 1])
                matched = pi[matched - 1]
    return result

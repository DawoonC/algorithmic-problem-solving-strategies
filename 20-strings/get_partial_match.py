def get_partial_match(s):
    """Finds length of longest substrings
    that is prefix and suffix at the same time.

    Args:
        s: string

    Returns:
        list of lenfth of longest of substring that is
        prefix and suffix at the same time in s[:i+1]
    """
    m = len(s)
    pi = [0] * m
    begin, matched = 1, 0
    while (begin + matched) < m:
        if s[begin + matched] == s[matched]:
            matched += 1
            pi[begin + matched - 1] = matched
        else:
            if matched == 0:
                begin += 1
            else:
                begin += (matched - pi[matched - 1])
                matched = pi[matched - 1]
    return pi

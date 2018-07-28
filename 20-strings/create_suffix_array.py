def compare(a, b, t, group):
    if group[a] != group[b]:
        return group[a] - group[b]
    return group[a + t] - group[b + t]


def create_suffix_array(s):
    n = len(s)
    t = 1
    group = [ord(e) for e in s]
    group.append(-1)
    perm = range(n)
    while t < n:
        perm.sort(cmp=lambda a, b: compare(a, b, t, group))
        if t * 2 >= n:
            break
        new_group = [0] * n
        new_group.append(-1)
        for i in xrange(1, n):
            if compare(perm[i - 1], perm[i], t, group):
                new_group[perm[i]] = new_group[perm[i - 1]] + 1
            else:
                new_group[perm[i]] = new_group[perm[i - 1]]
        t *= 2
        group = new_group
    return perm

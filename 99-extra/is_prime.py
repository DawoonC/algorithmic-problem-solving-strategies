from math import sqrt


def is_prime(n):
    if n < 4:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    sqrt_n = int(sqrt(n))
    for i in xrange(5, sqrt_n, 2):
        if n % i == 0:
            return False
    return True


def test():
    n_list = [
        (2, True),
        (3, True),
        (4, False),
        (13, True),
        (541, True),
        (179426445, False),
        (179426447, True),
        (32416189909, True),
        (32416189907, False),
    ]
    for (n, expected) in n_list:
        result = is_prime(n)
        assert result is expected
    print 'test success!'


if __name__ == '__main__':
    test()  # run

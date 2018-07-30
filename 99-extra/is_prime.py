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
    n = 2
    result = is_prime(n)
    assert result is True
    n = 3
    result = is_prime(n)
    assert result is True
    n = 4
    result = is_prime(n)
    assert result is False
    n = 13
    result = is_prime(n)
    assert result is True
    n = 541
    result = is_prime(n)
    assert result is True
    n = 179426445
    result = is_prime(n)
    assert result is False
    n = 179426447
    result = is_prime(n)
    assert result is True
    n = 32416189909
    result = is_prime(n)
    assert result is True
    n = 32416189907
    result = is_prime(n)
    assert result is False
    print 'test success!'


if __name__ == '__main__':
    test()  # run

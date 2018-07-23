from collections import defaultdict


def fib(n, cache=None):
    if cache is None:
        cache = defaultdict(lambda: None)
    if n < 2:
        return 1
    result = cache[n]
    if result is not None:
        return result
    result = cache[n] = fib(n - 1, cache) + fib(n - 2, cache)
    return result


# return nth number in fibonacci numbers
# using iterative dynamic programming
# use less memory than recursive one
def fib_w_iter_dp(n):
    if n < 2:
        return n
    # since fibonacci only needs n-2 numbers
    # cache with size of 3 is enough
    cache = [1, 1, None]
    for i in xrange(2, n + 1):
        cache[i % 3] = (cache[(i - 1) % 3] + cache[(i - 2) % 3])
    return cache[n % 3]

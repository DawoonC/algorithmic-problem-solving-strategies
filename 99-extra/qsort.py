from random import randrange


def qsort_inplace(array, left=0, right=None):
    if right is None:
        right = len(array) - 1
    if left >= right:
        return array
    p = randrange(left, right)
    array[p], array[right] = array[right], array[p]
    p = right
    i = left
    for j in xrange(left, right):
        if array[j] < array[p]:
            array[i], array[j] = array[j], array[i]
            i += 1
    array[i], array[p] = array[p], array[i]
    qsort_inplace(array, left, i - 1)
    qsort_inplace(array, i + 1, right)
    return array


def qsort(array):
    if not array:
        return array
    p = array[0]
    lo = qsort([e for e in array[1:] if e < p])
    hi = qsort([e for e in array[1:] if e >= p])
    return lo + [p] + hi

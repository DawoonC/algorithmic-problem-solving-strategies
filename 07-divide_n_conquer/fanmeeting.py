# Problem ID: FANMEETING
# https://algospot.com/judge/problem/read/FANMEETING

def readline():
    return raw_input()


def multiply(list_x, list_y):
    """
    Multiplies numbers in each position (without normalizing)
    e.g. 123 * 456 = multiply([3,2,1], [6,5,4]) = [18, 27, 28, 13, 4, 0, 0]
    """
    x_len, y_len = len(list_x), len(list_y)
    list_z = [0] * (x_len + y_len + 1)
    for i in range(x_len):
        for j in range(y_len):
            list_z[i+j] += list_x[i] * list_y[j]
    return list_z


def add_to(list_x, list_y, position):
    """
    Adds elements of list_y to list_x (list_x += list_y)
    """
    for j in range(position):
        list_y.insert(0, 0)
    for i in range(len(list_y)):
        if i < len(list_x):
            list_x[i] += list_y[i]
        else:
            list_x.append(list_y[i])


def sub_from(list_x, list_y):
    """
    Subtracts elements of list_y from list_x (list_x -= list_y)
    """
    for i in range(len(list_y)):
        if i < len(list_x):
            list_x[i] -= list_y[i]
        else:
            list_x.append(0 - list_y[i])


def karatsuba(list_x, list_y):
    """
    Karatsuba multiplication (without normalizing)
    """
    x_len, y_len = len(list_x), len(list_y)
    # swap if y is longer than x
    if x_len < y_len:
        karatsuba(list_y, list_x)
    # base case: when x or y is empty
    if x_len == 0 or y_len == 0:
        return []
    # base case: when x is fairly small
    if x_len <= 50:
        return multiply(list_x, list_y)
    half = x_len / 2
    x0, x1, y0, y1 = list_x[:half], list_x[half:], list_y[:min(half, y_len)], list_y[min(half, y_len):]
    # z2 = x1 * y1
    z2 = karatsuba(x1, y1)
    # z0 = x0 * y0
    z0 = karatsuba(x0, y0)
    # x0 = x0 + x1
    add_to(x0, x1, 0)
    # y0 = y0 + y1
    add_to(y0, y1, 0)
    # z1 = (x0 * y0) - z0 - z2
    z1 = karatsuba(x0, y0)
    sub_from(z1, z0)
    sub_from(z1, z2)
    # result = z0 + (10^half * z1) + (10^(half*2) * z2)
    result = [0] * len(z0)
    add_to(result, z0, 0)
    add_to(result, z1, half)
    add_to(result, z2, half+half)
    return result


def hugs(members, fans):
    """
    Count all possible hugs
    """
    enc_members = [1 if m == 'M' else 0 for m in members]
    enc_fans = [1 if f == 'M' else 0 for f in fans][::-1]
    result = karatsuba(enc_members, enc_fans)
    hug_cnt = 0
    for i in range(len(members)-1, len(fans)):
        if result[i] == 0:
            hug_cnt += 1
    return hug_cnt


def fanmeeting():
    total_tests = int(readline())
    for testcase in range(total_tests):
        members = readline()
        fans = readline()
        print hugs(members, fans)


if __name__ == '__main__':
    fanmeeting()  # run
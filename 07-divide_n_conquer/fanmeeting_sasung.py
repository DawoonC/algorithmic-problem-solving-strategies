# coding=utf-8
# https://algospot.com/judge/problem/read/FANMEETING

#Male = 1, Female = 0

def read():
    result = []
    text_list = list(raw_input())
    for text in text_list:
        if text == 'M':
            result.append(1)
        else:
            result.append(0)
    return result

def multiply(list_x, list_y):
    x_len, y_len = len(list_x), len(list_y)
    list_z = [0] * (x_len + y_len + 1)
    for i in range(x_len):
        for j in range(y_len):
            list_z[i+j] += list_x[i] * list_y[j]
    return list_z

def add_to(list_x, list_y, position):
    for j in range(position):
        list_y.insert(0, 0)
    for i in range(len(list_y)):
        if i < len(list_x):
            list_x[i] += list_y[i]
        else:
            list_x.append(list_y[i])


def sub_from(list_x, list_y):
    for i in range(len(list_y)):
        if i < len(list_x):
            list_x[i] -= list_y[i]
        else:
            list_x.append(0 - list_y[i])


def karatsuba(list_x, list_y):
    x_len, y_len = len(list_x), len(list_y)
    if x_len < y_len:
        karatsuba(list_y, list_x)
    if x_len == 0 or y_len == 0:
        return []

    if x_len <= 50:
        return multiply(list_x, list_y)
    half = x_len / 2
    x0, x1, y0, y1 = list_x[:half], list_x[half:], list_y[:min(half, y_len)], list_y[min(half, y_len):]

    z2 = karatsuba(x1, y1)

    z0 = karatsuba(x0, y0)
    add_to(x0, x1, 0)
    add_to(y0, y1, 0)
    z1 = karatsuba(x0, y0)
    sub_from(z1, z0)
    sub_from(z1, z2)
    result = [0] * len(z0)
    add_to(result, z0, 0)
    add_to(result, z1, half)
    add_to(result, z2, half+half)
    return result

def hugs(idol, fan):

    cal_idol = idol
    cal_fan = fan[::-1]
    print cal_idol, cal_fan
    result = karatsuba(cal_idol, cal_fan)
    count = 0
    for i in range(len(idol)-1, len(fan)):
        if result[i] == 0:
            count += 1

    return count


def fan_meeting():
    total_tests = int(raw_input())
    for testcase in range(total_tests):
        idol = read()
        fan = read()
        print(hugs(idol, fan))

fan_meeting()

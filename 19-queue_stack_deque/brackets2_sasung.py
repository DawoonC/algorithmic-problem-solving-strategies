# coding=utf-8
# Problem ID: BRACKETS2
# https://algospot.com/judge/problem/read/BRACKETS2


def bracket2(now_bracket):
    stack = []
    for item in now_bracket:
        try:
            if stack[-1] + item == '()' or stack[-1] + item == '[]' or stack[-1] + item == '{}':
                stack.pop()
            else:
                stack.append(item)
        except Exception:
            stack.append(item)

    if stack == []:
        return 'YES'
    else:
        return 'NO'


def runner():
    total_tests = int(raw_input())
    for testcase in range(total_tests):
        now_bracket = list(raw_input())
        print bracket2(now_bracket)

runner()
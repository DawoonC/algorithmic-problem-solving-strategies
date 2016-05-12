# Problem ID: BRACKETS2
# https://algospot.com/judge/problem/read/BRACKETS2
# 82ms

def readline():
    return raw_input()


def check_brackets(bracket_seq, bracket_map):
    stack = []
    for br in bracket_seq:
        if br in bracket_map:
            stack.append(br)
        else:
            if len(stack) == 0:
                return 'NO'
            elif bracket_map[stack[-1]] != br:
                return 'NO'
            else:
                stack.pop()
    return 'YES' if len(stack) == 0 else 'NO'


def brackets():
    total_tests = int(readline())
    bracket_map = {
        '(': ')',
        '{': '}',
        '[': ']'
    }
    for testcase in range(total_tests):
        bracket_seq = readline()
        print check_brackets(bracket_seq, bracket_map)


if __name__ == '__main__':
    brackets()  # run

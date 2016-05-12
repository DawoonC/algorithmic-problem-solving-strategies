# Problem ID: FENCE
# https://algospot.com/judge/problem/read/FENCE
# 565ms

def readline():
    return raw_input()


def solve_with_stack(fences, length):
    # stack for index of remaining fences
    remaining = []
    # append dummy 0 height fence to right end
    # 0 is added to ensure every remaining fence is removed at the end
    fences.append(0)
    result = 0
    for i in range(length+1):
        while len(remaining) != 0 and fences[remaining[-1]] >= fences[i]:
            j = remaining.pop()
            width = -1
            # if there is no remaining fences, 
            # then the width is equal to from left most to current position
            if len(remaining) == 0:
                width = i
            # if there is remaining fence,
            # then the width is equal to right most remaining fence to current position
            else:
                width = i - remaining[-1] - 1
            result = max(result, fences[j] * width)
        remaining.append(i)
    return result


def fence():
    total_tests = int(readline())
    for testcase in range(total_tests):
        length = int(readline())
        fences = map(int, readline().split())
        print solve_with_stack(fences, length)


if __name__ == '__main__':
    fence()  # run

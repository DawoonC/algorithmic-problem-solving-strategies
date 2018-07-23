# Problem ID: LUNCHBOX
# https://algospot.com/judge/problem/read/LUNCHBOX
# took 212ms


def readline():
    return raw_input()


def get_min_lunchtime(durations):
    cook_duaration = 0
    total = 0
    for (eat, cook) in durations:
        cook_duaration += cook
        total = max(total, cook_duaration + eat)
    return total


def lunchbox():
    total_tests = int(readline())
    for testcase in range(total_tests):
        n = int(readline())
        cook_durations = map(int, readline().split())
        eat_durations = map(int, readline().split())
        durations = sorted(zip(eat_durations, cook_durations), reverse=True)
        result = get_min_lunchtime(durations)
        print result


if __name__ == '__main__':
    lunchbox()  # run

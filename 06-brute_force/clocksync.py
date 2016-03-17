# Problem ID: CLOCKSYNC
# https://algospot.com/judge/problem/read/CLOCKSYNC

from collections import defaultdict

switches = [
    (0, 1, 2),
    (3, 7, 9, 11),
    (4, 10, 14, 15),
    (0, 4, 5, 6, 7),
    (6, 7, 8, 10, 12),
    (0, 2, 14, 15),
    (3, 14, 15),
    (4, 5, 7, 14, 15),
    (1, 2, 3, 4, 5),
    (3, 4, 5, 9, 13)
]

def readline():
    return raw_input()


def check_clocks(clock_dict):
    """
    Check if all clock is set to 12.

    Args:
        clock_dict: a dictionary which tracks time on each clocks
    Returns:
        True if clock is sync,
        False if not sync
    """
    return clock_dict.values().count(12) == 16


def sync(clocks, clock_dict, switch):
    """
    Recursively find minimum switch count to get clocksync.

    Args:
        clocks: a list representing initial clock status
        clock_dict: a dictionary which tracks time on each clocks
        switch: switch to push
    Returns:
        minimum switch count
    """
    # check if clock is sync when reach to the final switch
    if switch == 10:
        return 0 if check_clocks(clock_dict) else float('inf')
    # recursively find minimum switch count to get clocksync
    min_switch = float('inf')
    for switch_count in range(4):
        min_switch = min(min_switch, sync(clocks, clock_dict, switch+1) + switch_count)
        for clock in switches[switch]:
            clock_dict[clock] += 3
            if clock_dict[clock] == 15:
                clock_dict[clock] = 3
    return min_switch


def clocksync():
    total_tests = int(readline())
    for testcase in range(total_tests):
        clocks = map(int, readline().split())
        if clocks[14] != clocks[15] or clocks[8] != clocks[12]:
            print -1
        clock_dict = {}
        for clock in range(16):
            clock_dict[clock] = clocks[clock]
        inf = float('inf')
        min_switch = sync(clocks, clock_dict, 0)
        if min_switch == inf:
            print -1
        else:
            print min_switch


if __name__ == '__main__':
    clocksync()  # run
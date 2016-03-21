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


def is_equal_list(_list, for_clocks=False):
    """
    Check if all items in a list are equal.

    Args:
        _list: a list to check
        for_clocks: a boolean value to handle clock case specifically
    Returns:
        True if all items are equal,
        False if not
    """
    return _list.count(12) == 16 if for_clocks else _list.count(_list[0]) == len(_list)


def push_switch(switch, clock_dict, push_count):
    """
    Push the given switch and make changes to the clocks.

    Args:
        switch: switch to push
        clock_dict: a dictionary which tracks time on each clocks
        push_count: a number of push action to take
    """
    for e in range(push_count):
        for clock in switches[switch]:
            clock_dict[clock] += 3
            if clock_dict[clock] == 15:
                clock_dict[clock] = 3


def remove_pushed_switches(pushed_switches, switch_dict):
    """
    Remove pushed switches from the switch dictionary.

    Args:
        pushed_switches: a list of switches pushed
        switch_dict: a dictionary which has clocks as keys, and linked switches as values
    """
    for key in switch_dict.keys():
        for switch in pushed_switches:
            if switch in switch_dict[key]:
                switch_dict[key].pop(switch_dict[key].index(switch))


def faster_sync(switch_dict, clock_dict):
    """
    Sync the clocks by eliminating clock-switch link that has fixed number of push count.

    Args:
        switch_dict: a dictionary which has clocks as keys, and linked switches as values
        clock_dict: a dictionary which tracks time on each clocks
    Returns:
        minimum switch count
    """
    pushed_switches = set()
    fixed_clocks = set()
    count = 0
    # while there are still switch left to push
    while not is_equal_list(switch_dict.values()):
        for (clock, switch_list) in switch_dict.items():
            # if a clock has only one switch linked,
            # then it means it has fixed number of push count
            if len(switch_list) == 1:
                count += ((12 - clock_dict[clock]) / 3)
                push_switch(switch_list[0], clock_dict, (12 - clock_dict[clock]) / 3)
                pushed_switches.add(switch_list[0])
                fixed_clocks.add(clock)
        # if there was only one switch pushed in this iteration,
        # then all clocks with fixed count must have equal values
        if len(pushed_switches) == 1 and not is_equal_list(map(lambda clock: clock_dict[clock], fixed_clocks)):
            return float('inf')
        # if all clocks are sync, then return the count
        if is_equal_list(clock_dict.values(), True):
            return count
        # remove pushed switches and reset
        remove_pushed_switches(pushed_switches, switch_dict)
        pushed_switches.clear()
        fixed_clocks.clear()
    # if all clocks are sync, then return the count
    if is_equal_list(clock_dict.values(), True):
        return count
    else:
        return float('inf')


def clocksync():
    total_tests = int(readline())
    for testcase in range(total_tests):
        clocks = map(int, readline().split())
        if clocks[14] != clocks[15] or clocks[8] != clocks[12]:
            print -1
        switch_dict = defaultdict(list)
        for switch in range(10):
            for clock in switches[switch]:
                switch_dict[clock].append(switch)
        clock_dict = {}
        for clock in range(16):
            clock_dict[clock] = clocks[clock]
        inf = float('inf')
        min_switch = faster_sync(switch_dict, clock_dict)
        if min_switch == inf:
            print -1
        else:
            print min_switch


if __name__ == '__main__':
    clocksync()  # run
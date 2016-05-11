# coding=utf-8
# Problem ID: JOSEPHUS
# https://algospot.com/judge/problem/read/JOSEPHUS


# recursion
def josephus2(people_list, death_number, next_die):
    people_list.pop(next_die)
    if len(people_list) == 2:
        return ' '.join(map(str, people_list))
    next_die = next_die + death_number - 1
    next_die = next_die % len(people_list) if next_die >= len(people_list) else next_die
    return josephus2(people_list, death_number, next_die)


# non recursion
def josephus(people_list, death_number):
    people_list.remove(people_list[0])
    idx = death_number - 1
    while len(people_list) > 2:
        if idx > len(people_list) -1:
            idx -= len(people_list)

        people_list.remove(people_list[idx])
        idx += death_number-1

    return people_list

def runner():
    total_tests = int(raw_input())
    for testcase in range(total_tests):
        people_number, death_number = map(int, raw_input().split())
        # print josephus(range(1,people_number+1), death_number)
        print josephus2(range(1,people_number+1), death_number,0)

runner()

'''
2
6 3
40 3
'''
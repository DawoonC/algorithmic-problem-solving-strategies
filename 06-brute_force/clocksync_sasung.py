#coding=utf-8
# https://algospot.com/judge/problem/read/ClOCKSYNC

switches = [
    [0,1,2],
    [3,7,9,11],
    [4,10,14,15],
    [0,4,5,6,7],
    [6,7,8,10,12],
    [0,2,14,15],
    [3,14,15],
    [4,5,7,14,15],
    [1,2,3,4,5],
    [3,4,5,9,13]
]

def check_clocks(clock_dict):
    return clock_dict.values().count(12) == 16

def change_clock(clock_dict, switch):
    # print (clock_dict, switch)
    # print(switch)
    if switch == 10:
        return 0 if check_clocks(clock_dict) else float('inf')

    min_switch = float('inf')
    for i in range(4):
        min_switch = min(min_switch, i + change_clock(clock_dict, switch+1))
        for clock in switches[switch]:
            clock_dict[clock] += 3
            if clock_dict[clock] == 15:
                clock_dict[clock] = 3

    return min_switch

a = [12, 6, 6, 6, 6, 6, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12]
b = {0: 12, 1: 6, 2: 6, 3: 6, 4: 6, 5: 6, 6: 12, 7: 12, 8: 12, 9: 12, 10: 12, 11: 12, 12: 12, 13: 12, 14: 12, 15: 12}

print change_clock(b, -1)


def clock_sync():
    total_tests = int(raw_input())
    for testcase in range(total_tests):
        clocks = [int(x) for x in raw_input().split()]
        clock_dict = {}
        for clock in range(16):
            clock_dict[clock] = clocks[clock]
        inf = float('inf')
        min = change_clock(clock_dict, -1)
        if min ==inf:
            print -1
        else:
            print min

# clock_sync()


# def change_clock(now, total_count):
#     if total_count > 10:
#         print('fail')
#         return False
#
#     print(now, total_count)
#     tmp = []
#     both_max = 0
#     num = 0
#     flag = False
#
#     for idx, each in enumerate(now):
#         if each != 12:
#             tmp.append(idx)
#
#     if tmp == []:
#         print('finish')
#         print(total_count)
#         return True
#
#     # print('go')
#     for s in switch:
#         if set(switch[s]).issubset(tmp):
#             for click in switch[s]:
#                 now[click] += 3
#                 if now[click] > 12:
#                     now[click] = 3
#             total_count += 1
#             flag = True
#             change_clock(now, total_count)
#
#         else:
#             both_number = len(set(switch[s]).intersection(set(tmp)))
#             if both_max < both_number:
#                 both_max = both_number
#                 num = s
#
#     if flag == False:
#         # print(tmp, switch[num])
#         for click in switch[num]:
#             now[click] += 3
#             if now[click] > 12:
#                 now[click] = 3
#
#         total_count+=1
#         print(now, total_count)
#         change_clock(now, total_count)
#coding=utf-8
# https://algospot.com/judge/problem/read/PICNIC
from collections import defaultdict

def count_pairings(taken, friends, students):

    # 없거나 false 일 경우 first_not_taken 초기화
    first_not_taken = -1
    for student in range(students):
        if not taken[student]:
            first_not_taken = student
            break
    # 적절한 쌍을 찾은 경우 return 1이 되면서 count ++ 됨
    if first_not_taken == -1:
        return 1
    # recursively find all possible pairings
    count = 0
    for pair_with in range(first_not_taken+1, students):
        if not taken[pair_with] and pair_with in friends[first_not_taken]:
            taken[first_not_taken] = taken[pair_with] = True
            print taken
            count += count_pairings(taken, friends, students)
            print("count : "+ str(count))
            taken[first_not_taken] = taken[pair_with] = False
            print taken
    return count


def picnic():
    total_tests = int(raw_input())
    for testcase in range(total_tests):
        total_students, total_pairs = map(int, raw_input().split())
        temp = raw_input().split()
        friends = defaultdict(list)

        #누구끼리 친구인지 defaultdict의 리스트 형태로 저장함
        for i in range(0, len(temp), 2):
            friends[int(temp[i])].append(int(temp[i+1]))
            friends[int(temp[i+1])].append(int(temp[i]))

        #짝이 있는 지 확인하는 defaultdict를 boolean 형태로 저장
        taken = defaultdict(bool)
        print count_pairings(taken, friends, total_students)

picnic()
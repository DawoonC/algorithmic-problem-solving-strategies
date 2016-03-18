# Problem ID: PICNIC
# https://algospot.com/judge/problem/read/PICNIC

from collections import defaultdict

def readline():
    return raw_input()


def count_pairings(taken, friends, students):
    """
    Recursively count all pairings of friend pairs.

    Args:
        taken: a dictionary which tracks whether each student is taken for pair up
        friends: a dictionary which has students as keys, and their friends as values
        students: a list of students
    Returns:
        a number of all possible pairings of friend pairs
    """
    # find a student that hasn't been taken yet
    first_not_taken = -1
    for student in students:
        if not taken[student]:
            first_not_taken = student
            break
    # if there is no student left to select,
    # then it means we found a pairing, so return 1
    if first_not_taken == -1:
        return 1
    # recursively find all possible pairings
    count = 0
    for pair_with in range(first_not_taken+1, len(students)):
        if not taken[pair_with] and pair_with in friends[first_not_taken]:
            taken[first_not_taken] = taken[pair_with] = True
            count += count_pairings(taken, friends, students)
            taken[first_not_taken] = taken[pair_with] = False
    return count


def picnic():
    total_tests = int(readline())
    for testcase in range(total_tests):
        total_students, total_pairs = map(int, readline().split())
        temp = readline().split()
        friends = defaultdict(list)
        for i in range(0, len(temp), 2):
            friends[int(temp[i])].append(int(temp[i+1]))
            friends[int(temp[i+1])].append(int(temp[i]))
        taken = defaultdict(bool)
        print count_pairings(taken, friends, range(total_students))


if __name__ == '__main__':
    picnic()  # run
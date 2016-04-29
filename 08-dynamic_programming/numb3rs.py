# Problem ID: NUMB3RS
# https://algospot.com/judge/problem/read/NUMB3RS
# timeout

from collections import defaultdict

def readline():
    return raw_input()


def search(current_vil, today, destination_vil, num_of_vil, d_day, vil_matrix, vildict):
    if today == d_day:
        return 1.0 if current_vil == destination_vil else 0.0
    result = vildict[(current_vil,today)]
    if result > -0.5:
        return result
    result = 0.0
    degree = float(vil_matrix[current_vil].count(1))
    for i in range(num_of_vil):
        if vil_matrix[current_vil][i] == 1:
            result += search(i, today+1, destination_vil, num_of_vil, d_day, vil_matrix, vildict) / degree
    vildict[(current_vil,today)] = result
    return result


def reverse_search(current_vil, today, prison_vil, num_of_vil, vil_matrix, vildict):
    if today == 0:
        return 1.0 if current_vil == prison_vil else 0.0
    result = vildict[(current_vil,today)]
    if result > -0.5:
        return result
    result = 0.0
    for i in range(num_of_vil):
        degree = float(vil_matrix[i].count(1))
        if vil_matrix[current_vil][i] == 1:
            result += reverse_search(i, today-1, prison_vil, num_of_vil, vil_matrix, vildict) / degree
    vildict[(current_vil,today)] = result
    return result


def numb3rs():
    total_tests = int(readline())
    for testcase in range(total_tests):
        num_of_vil, d_day, prison_vil = map(int, readline().split())
        vil_matrix = []
        for i in range(num_of_vil):
            vil_matrix.append(map(int, readline().split()))
        num_of_vil_to_calc = int(readline())
        vil_to_calc = map(int, readline().split())
        result = []
        vildict = defaultdict(lambda:-1.0)
        for destination_vil in vil_to_calc:
            # vildict = defaultdict(lambda:-1.0)
            # result.append(search(prison_vil, 0, destination_vil, num_of_vil, d_day, vil_matrix, vildict))
            result.append(reverse_search(destination_vil, d_day, prison_vil, num_of_vil, vil_matrix, vildict))
        print ' '.join(map(str, result))


if __name__ == '__main__':
    numb3rs()  # run
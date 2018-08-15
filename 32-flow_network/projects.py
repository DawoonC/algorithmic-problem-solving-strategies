from collections import defaultdict
from ford_fulkerson import ford_fulkerson


def readline(inputs):
    return inputs.pop(0)


def get_max_profit(profits, prices, needed_equipments, n_business, n_equipment):
    n_v = 2 + n_business + n_equipment
    capacity = defaultdict(lambda: defaultdict(int))
    for i in xrange(n_business):
        capacity[0][2 + i] = profits[i]
    for i in xrange(n_equipment):
        capacity[2 + n_business + i][1] = prices[i]
    for i in xrange(n_business):
        for j in xrange(n_equipment):
            if needed_equipments[i][j] == 1:
                capacity[2 + i][2 + n_business + j] = float('inf')
    result = ford_fulkerson(0, 1, capacity, range(n_v))
    return sum(profits) - result


def projects():
    inputs = [
        '2',
        '2 2',
        '10 10',
        '5 10',
        '1 0',
        '1 1',
        '5 5',
        '260 60 140 350 500',
        '250 100 150 300 100',
        '1 0 0 0 0',
        '1 1 1 0 0',
        '0 0 1 1 0',
        '0 0 0 1 0',
        '0 0 0 1 1',
    ]
    total_tests = int(readline(inputs))
    for _ in xrange(total_tests):
        n_business, n_equipment = map(int, readline(inputs).split())
        profits = map(int, readline(inputs).split())
        prices = map(int, readline(inputs).split())
        needed_equipments = []
        for _ in xrange(n_business):
            equipments = map(int, readline(inputs).split())
            needed_equipments.append(equipments)
        result = get_max_profit(profits, prices, needed_equipments, n_business, n_equipment)
        print result


if __name__ == '__main__':
    projects()  # run

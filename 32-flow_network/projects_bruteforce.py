def readline(inputs):
    return inputs.pop(0)


def get_max_profit(business, purchased, profits, prices, needed_equipments, n_equipment, n_business):
    if business >= n_business:
        return 0
    profit = profits[business]
    new_purchased = set()
    price = 0
    for i in xrange(n_equipment):
        if needed_equipments[business][i] == 1 and i not in purchased:
            price += prices[i]
            new_purchased.add(i)
    result = 0
    actual_profit = profit - price
    result = max(result, actual_profit + get_max_profit(business + 1, purchased | new_purchased, profits, prices, needed_equipments, n_equipment, n_business))
    result = max(result, get_max_profit(business + 1, purchased, profits, prices, needed_equipments, n_equipment, n_business))
    return result


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
        result = get_max_profit(0, set(), profits, prices, needed_equipments, n_equipment, n_business)
        print result


if __name__ == '__main__':
    projects()  # run

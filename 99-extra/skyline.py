import heapq


def skyline(buildings):
    if not buildings:
        return []
    points = []
    for l, r, h in buildings:
        points.append([l, -h])
        points.append([r, h])
    # sort the points to ensure that all points are sorted from left to right
    points.sort()
    result = []
    queue = [0]
    prev = 0
    for e in points:
        if e[1] < 0:
            # whenever we see start point of the building
            # we put the height of the building into the heapq
            heapq.heappush(queue, e[1])
        else:
            # if we arrive at the end point of the building
            # we remove the height of the building from the heapq
            if queue[0] == -e[1]:
                heapq.heappop(queue)
            else:
                queue.remove(-e[1])
                heapq.heapify(queue)
        curr = queue[0]
        if curr != prev:
            # if the tallest building in the heapq changes
            # then we need to put that into the final result
            result.append([e[0], -curr])
            prev = curr
    return result


def faster_skyline(buildings):
    if not buildings:
        return []
    points = []
    for l, r, h in buildings:
        points.append([l, -h, r])
        points.append([r, 0, 0])
    points.sort()
    result = [(0, 0)]
    queue = [(0, float('inf'))]
    for l, h, r in points:
        while l >= queue[0][1]:
            heapq.heappop(queue)
        if h:
            # since all end points are stored with 0 heights
            # truthy h means it's a start point
            heapq.heappush(queue, (h, r))
        if result[-1][1] + queue[0][0]:
            # positive h + negative h
            # if it's 0, then it means they are same height
            # and we ignore it
            result.append([l, -queue[0][0]])
    return result[1:]


def test():
    # Input: [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
    # Output: [[2, 10],[3, 15],[7, 12],[12, 0],[15, 10],[20 8],[24, 0]]
    buildings = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
    expected = [[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]]
    result = skyline(buildings)
    assert result == expected
    result = faster_skyline(buildings)
    assert result == expected
    print 'test success!'


if __name__ == '__main__':
    test()  # run

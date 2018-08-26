# Given an array of meeting time intervals consisting of
# start and end times [[s1,e1],[s2,e2],...] (si < ei),
# find the minimum number of conference rooms required.

import heapq


class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


def create_intervals(times):
    return [Interval(s, e) for s, e in times]


def min_meeting_rooms(intervals):
    sorted_intervals = sorted(intervals, key=lambda itv: (itv.start, itv.end))
    rooms = []
    for itv in sorted_intervals:
        if not rooms:
            rooms.append((itv.end, itv.start))
            continue
        if itv.start < rooms[0][0]:
            heapq.heappush(rooms, (itv.end, itv.start))
            continue
        heapq.heappop(rooms)
        heapq.heappush(rooms, (itv.end, itv.start))
    return len(rooms)


def test():
    # Input: [[0, 30],[5, 10],[15, 20]]
    # Output: 2
    times = [[0, 30],[5, 10],[15, 20]]
    intervals = create_intervals(times)
    expected = 2
    result = min_meeting_rooms(intervals)
    assert result == expected
    # Input: [[7,10],[2,4]]
    # Output: 1
    times = [[7,10],[2,4]]
    intervals = create_intervals(times)
    expected = 1
    result = min_meeting_rooms(intervals)
    assert result == expected
    print 'test success!'


if __name__ == '__main__':
    test()  # run

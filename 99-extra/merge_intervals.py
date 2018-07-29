class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


def merge_intervals(intervals):
    s_intervals = sorted(intervals, key=lambda x: x.start)
    result = []
    for itv in s_intervals:
        if not result or result[-1].end < itv.start:
            result.append(itv)
        else:
            result[-1].end = max(result[-1].end, itv.end)
    return result


def test():
    # Input: [[1,3],[2,6],[8,10],[15,18]]
    # Output: [[1,6],[8,10],[15,18]]
    a = [[1,3],[2,6],[8,10],[15,18]]
    intervals = [Interval(s, e) for (s, e) in a]
    result = merge_intervals(intervals)
    assert [[e.start, e.end] for e in result] == [[1,6],[8,10],[15,18]]
    # Input: [[1,4],[4,5]]
    # Output: [[1,5]]
    a = [[1,4],[4,5]]
    intervals = [Interval(s, e) for (s, e) in a]
    result = merge_intervals(intervals)
    assert [[e.start, e.end] for e in result] == [[1,5]]
    print 'test success!'


if __name__ == '__main__':
    test()  # run

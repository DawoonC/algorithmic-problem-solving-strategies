class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


def can_attend_all_meetings(intervals):
    s_intervals = sorted(intervals, key=lambda x: x.start)
    result = []
    for itv in s_intervals:
        if not result or result[-1].end <= itv.start:
            result.append(itv)
        else:
            return False
    return True


def test():
    # Input: [[0,30],[5,10],[15,20]]
    # Output: false
    a = [[0,30],[5,10],[15,20]]
    intervals = [Interval(s, e) for (s, e) in a]
    result = can_attend_all_meetings(intervals)
    assert result is False
    # Input: [[7,10],[2,4]]
    # Output: True
    a = [[7,10],[2,4]]
    intervals = [Interval(s, e) for (s, e) in a]
    result = can_attend_all_meetings(intervals)
    assert result is True
    print 'test success!'


if __name__ == '__main__':
    test()  # run

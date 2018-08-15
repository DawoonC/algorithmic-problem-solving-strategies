# Problem ID: MATCHFIX
# https://algospot.com/judge/problem/read/MATCHFIX
# took 704ms

from collections import defaultdict
from ford_fulkerson import ford_fulkerson


def readline():
    return raw_input()


def can_win_with(total_wins, wins, matches, n_players, n_matches):
    if max(wins[1:]) >= total_wins:
        return False
    n_v = 2 + n_matches + n_players
    # 0: source
    # 1: sink
    # range(2, 2 + n_matches): matches
    # range(2 + n_matches, 2 + n_matches + n_players): players
    capacity = defaultdict(lambda: defaultdict(int))
    for i in xrange(n_matches):
        # from source to each match
        capacity[0][2 + i] = 1
        for j in xrange(2):
            # from each match to each player
            capacity[2 + i][2 + n_matches + matches[i][j]] = 1
    for i in xrange(n_players):
        max_win = total_wins if i == 0 else total_wins - 1
        # from each player to sink
        capacity[2 + n_matches + i][1] = max_win - wins[i]
    result = ford_fulkerson(0, 1, capacity, range(n_v))
    return result == n_matches


def matchfix():
    total_tests = int(readline())
    for _ in xrange(total_tests):
        n_players, n_matches = map(int, readline().split())
        wins = map(int, readline().split())
        matches = []
        max_win = 0
        for _ in xrange(n_matches):
            u, v = map(int, readline().split())
            matches.append((u, v))
            if u == 0 or v == 0:
                max_win += 1
        curr_win = wins[0]
        result = False
        min_win = -1
        for cand in xrange(curr_win, curr_win + max_win + 1):
            result = can_win_with(cand, wins, matches, n_players, n_matches)
            if result is True:
                min_win = cand
                break
        print min_win


if __name__ == '__main__':
    matchfix()  # run

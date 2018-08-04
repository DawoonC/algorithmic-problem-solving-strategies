# Problem ID: EDITORWARS
# https://algospot.com/judge/problem/read/EDITORWARS
# took > 4000ms

from disjoint_set import DisjointSet


def readline():
    return raw_input()


def editorwars():
    total_tests = int(readline())
    for testcase in xrange(total_tests):
        n_users, n_cmts = map(int, readline().split())
        group_set = DisjointSet(n_users)
        contradiction_at = None
        dis_cnt = 0
        for i in xrange(n_cmts):
            reaction, user_a, user_b = readline().split()
            user_a, user_b = int(user_a), int(user_b)
            if reaction == 'ACK':
                group_set.merge(user_a, user_b)
            else:
                dis_cnt += 1
                if contradiction_at is None and group_set.find(user_a) == group_set.find(user_b):
                    contradiction_at = i + 1
        if contradiction_at is not None:
            print 'CONTRADICTION AT', contradiction_at
        else:
            print 'MAX PARTY SIZE IS', n_users - dis_cnt


if __name__ == '__main__':
    editorwars()  # run

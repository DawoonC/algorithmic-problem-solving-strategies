# coding=utf-8
# Problem ID: TRAVERSAL
# https://algospot.com/judge/problem/read/TRAVERSAL

def print_post_order(pre_order, in_order, post_order):

    size = len(pre_order)

    if size == 0:
        return

    root = pre_order[0]

    left = in_order.index(root)
    print 'root', root
    print 'a',(pre_order[1:left+1], in_order[:left], post_order)
    print_post_order(pre_order[1:left+1], in_order[:left], post_order)
    print 'b',(pre_order[left+1:], in_order[left+1:], post_order)
    print_post_order(pre_order[left+1:], in_order[left+1:], post_order)
    # print 'root',root
    post_order.append(root)
    return

    # right = len(in_order[in_order.index(root)+1:])

    # print print_post_order(slice(pre_order, 1, left+1), slice(in_order, 0, left))
    # print print_post_order(slice(pre_order, left+1, size), slice(in_order, left+1, size))

    # result1 = pre_order[1:left+1][-1]
    # result2 = in_order[in_order.index(result1)-1]
    # result3 = in_order[in_order.index(result1)+1]
    #
    # result4 = in_order[in_order.index(root)+1]
    # result5 = pre_order[pre_order.index(result4)+1]
    # result6 = pre_order[pre_order.index(result4)-1]
    #
    # print result1, result2, result3, result4, result5, result6, root


def runner():
    total_tests = int(raw_input())
    for testcase in range(total_tests):
        node_number = int(raw_input())
        pre_order = map(str, raw_input().split())
        in_order = map(str, raw_input().split())
        post_order = []
        print_post_order(pre_order, in_order, post_order)
        # print post_order
        print ' '.join(post_order)

runner()

'''
1
7
27 16 9 12 54 36 72
9 12 16 27 36 54 72
'''
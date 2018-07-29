# Problem ID: TRAVERSAL
# https://algospot.com/judge/problem/read/TRAVERSAL
# 31ms


def readline():
    return raw_input()


def calculate_postorder(preorder, inorder, postorder):
    tree_length = len(preorder)
    if tree_length == 0:
        return
    # the first item of preorder is always the root
    root = preorder[0]
    # since the root is visited after traversing all left subtree of the root
    # in inorder, we can partition left and right subtree with root index 
    l_partition = inorder.index(root)
    print l_partition
    calculate_postorder(preorder[1:l_partition + 1], inorder[:l_partition], postorder)
    calculate_postorder(preorder[l_partition + 1:], inorder[l_partition + 1:], postorder)
    print postorder
    # the root is visited after traversing all the subtrees in postorder
    postorder.append(root)
    return


def traversal():
    total_tests = int(readline())
    for testcase in range(total_tests):
        readline()
        preorder = readline().split()
        inorder = readline().split()
        postorder = []
        calculate_postorder(preorder, inorder, postorder)
        print ' '.join(postorder)


if __name__ == '__main__':
    traversal()  # run

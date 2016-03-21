# Problem ID: QUADTREE
# https://algospot.com/judge/problem/read/QUADTREE

def readline():
    return raw_input()


def flip_quadtree(compressed):
    """
    Flip quadtree by recursively flipping inner subtrees.

    Args:
        compressed: a string representing compressed quadtree to flip
    Returns:
        top & bottom flipped quadtree
    """
    # if compressed quadtree does not start with 'x'
    # then it does not need any flipping
    if not compressed.startswith('x'):
        return compressed
    pixels = []
    p_index = 1
    # since it's a quadtree, it can be divided into 4 subtrees
    # if subtree starts with 'x', then it will be flipped as well
    for _ in range(4):
        if compressed[p_index] != 'x':
            pixels.append(compressed[p_index])
            p_index += 1
        else:
            sub_flipped = flip_quadtree(compressed[p_index:])
            pixels.append(sub_flipped)
            p_index += len(sub_flipped)
    # flip top & bottom
    return 'x' + pixels[2] + pixels[3] + pixels[0] + pixels[1]


def quadtree():
    total_tests = int(readline())
    for testcase in range(total_tests):
        compressed = readline()
        print flip_quadtree(compressed)


if __name__ == '__main__':
    quadtree()  # run
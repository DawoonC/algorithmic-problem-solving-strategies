#coding=utf-8
# https://algospot.com/judge/problem/read/QUADTREE

def decompressed(compressed):
    result = []
    pos = 1

    if not compressed[0] == 'x':
        return compressed

    for i in range(4):
        if compressed[pos] != 'x':
            result.append(compressed[pos])
            pos += 1
        else:
            recursion = decompressed(compressed[pos:])
            result.append(recursion)
            pos += len(recursion)
    return 'x' + result[2] + result[3] + result[0] + result[1]

# print decompressed('xbwxwbbwb')

def quadtree():
    total_tests = int(raw_input())
    for testcase in range(total_tests):
        compressed = str(raw_input())
        print decompressed(compressed)

quadtree()
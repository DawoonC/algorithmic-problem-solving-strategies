#coding=utf-8
# https://algospot.com/judge/problem/read/BOGGLE
"""
1
URLPM
XPRET
GIAET
XTNZY
XOQRS
6
PRETTY
GIRL
REPEAT
KARA
PANDORA
GIAZAPX
"""

dx = [-1, -1, -1, 1, 1, 1, 0, 0]
dy = [-1, 0, 1, -1, 0, 1, -1, 1]

def hasWord(board, y, x, word):
    if(board[y][0][x] != word[0]):
        return False

    if(len(word) == 1):
        return True

    for i in range(0,8):
        if(y+dy[i] < 0 or x+dx[i] < 0 or y+dy[i] > 4 or x+dx[i] > 4):
            continue
        if(board[y+dy[i]][0][x+dx[i]] == word[1]):
            result = hasWord(board, y+dy[i], x+dx[i], word[1:])
            if result:
                return True

def boggle():
    case = int(raw_input())
    board=[]

    for i in range(0, case):
        for j in range(0,5):
            board.append([str(x) for x in raw_input().split()])

    checkCount = int(raw_input())
    for n in range(0,checkCount):
        word = raw_input()
        result = []
        for row in range(0,5):
            for col in range(0,5):
                result.append(hasWord(board, row, col, word))
        if True in result:
            print 'YES'
        else:
            print 'NO'

boggle()
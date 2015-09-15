print "Let's play a game. Enter a series of only zeroes and ones to build a board with the most solid rows, and \
and colums of either ones or zeroes! Enter your numbers (no spaces)"
string = raw_input()
maxColumnScore = [0, 0]
maxRowScore = [0, 0]


def buildBoard(myStr, factor):
    board = []
    i = 0
    while i < len(myStr):
        board.append(myStr[i:(i+factor)])
        i = i + factor
    return board


def getBoards(myStr):
    num = len(myStr)
    boards = set()
    for x in range(2, num):
        if num % x == 0:
            b = buildBoard(myStr, x)
            scoreBoard(b)
    return boards


def scoreBoard(board):
    scoreX = 0
    scoreY = len(board[0])  
    cols = set()  
    for y in range(len(board)):
        if '0' not in board[y]:
            scoreX = scoreX + 1  
        for x in range(len(board[0])):
            if board[y][x] == '0':
                
                cols.add(x)
    scoreY = scoreY - len(cols)
                
    setMaxScore(scoreX, scoreY, board)


def setMaxScore(scoreX, scoreY, board):
    if maxRowScore[0] < scoreX:
        maxRowScore[0] = scoreX
        maxRowScore[1] = scoreY
    if maxColumnScore[1] < scoreY:
        maxColumnScore[0] = scoreX
        maxColumnScore[1] = scoreY

u = getBoards(string)


def printRes(maxScore):
    print "With ", maxScore[0], " solid rows and ", maxScore[1], " solid columns"

if maxColumnScore[1] > maxRowScore[0]:
    printRes(maxColumnScore)
elif maxRowScore[0] < maxColumnScore[1]:
    printRes(maxRowScore)
else:
    print "It's a tie!"
    printRes(maxColumnScore)
    printRes(maxRowScore)

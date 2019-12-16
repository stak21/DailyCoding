# Success: 12/15/19 11:49 886ms
def isSolved(board):
    # Requirements:
    #   Return the result of the tictactoe board
    #   1 : O
    #   2: X
    #   0: Tie
    #   -1: Incomplete
    # I/O:
    #   [
    #       [1, 1, 1],
    #       [2,2, 0],
    #       [2, 1, 2]
    #   ]   Should result in 1
    # Process:
    #   Return 1: When 3 1's are in a line
    #   Return 2: When 3 2's are in a line
    #   Thoughts:    The logic should be the same for the first two, so we can just solve for one logic
    #                      One idea is to iterate through all the possible patterns and if a pattern has all  of (1, 2) then return that number
    #                       Patterns: horizontal - an array with all the same number(1, 2)
    #                                           vertical - check the values at [0][x], [1][x], [2][x] 
    #                                             diagonal - check the values at [0][0], [1][1], [2][2] and [0][2], [1][1],[2][0]
    #   Return -1: If there are still 0's on the board and the first conditions have not been met
    #   Return 0:  If there are no 0's on the board and all conditions above have been met

    def readHorizontal(arr):
        if 0 in arr:
            return -1
        sums= sum(arr)
        if sums == 3:
            return 1
        if sums == 6:
            return 2
        return 0

    def readVertical(board):
        for i in range(3):
            # checks 1
            if 0 in [board[0][i], board[1][i], board[2][i]]:
                return -1
            sums = board[0][i] + board[1][i] + board[2][i]
            if sums == 3:
                return 1
            if sums == 6:
                return 2
        return 0
    def readDiagonal(board):
        if 0 in [board[0][0], board[1][1], board[2][2]] and 0 in [board[0][2], board[1][1], board[2][0]]:
            return -1
        sum1 =  sum([board[0][0], board[1][1], board[2][2]])
        sum2 = sum([board[0][2], board[1][1], board[2][0]])
        if sum1 == 3 or sum2 == 3:
            return 1
        if sum1 == 6 or sum2 == 6:
            return 2
        return 0
    total = 0
    # check horizontal
    for row in board:
        res = readHorizontal(row)
        total += res
        if res > 0:
            return res
    # check vertical
    res = readVertical(board)
    total += res
    if res > 0:
        return res
    # check diagonal
    res = readDiagonal(board)
    total += res
    if res > 0 :
        return res
    if total < 0:
        return -1
    return 0

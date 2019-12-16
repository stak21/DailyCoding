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
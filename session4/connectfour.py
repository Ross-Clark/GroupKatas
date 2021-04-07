""" Accept 2D array representing counters """
# Function takes array matrix as argument

def connectFour(board):

# Check array matrix actually represents connect four board
    # Check each row is 7 across
    # Check there are 6 rows
    if len(board) != 6:
        print("That isn't a valid board")
        return 1

    for row in board:
        if len(row) != 7:
            print("That isn't a valid board")
            return 1

    """ Determine who is the winner """
    # Check for a horizontal win

    # In each horizontal array, just check for four consecutive identical counters
    # Sent to winCheck
    hor_winner = winCheck(board)

    if hor_winner:
        return hor_winner

# Check for a vertical win
    # Make lists that are vertical slices through the array matrix
    vertical_slices = [[],[],[],[],[],[],[]]

    for row in board:
        for slot_no, slot in enumerate(row):
            vertical_slices[slot_no].append(slot)

    # Treat them like horizontal arrays to check for a win
    # Sent to winCheck
    ver_winner = winCheck(vertical_slices)

    if ver_winner:
        return ver_winner

# Check for diagonal wins
    # For each counter on a row, see if there is the same counter in +1||-1 position on the next row down
    # If there isn't, stop and move on to the next counter
    
    for rowNo, row in enumerate(board):
        # Only need to check first three rows for potential diagonal wins
        if rowNo > 2:
            break

        for slotNo, slot in enumerate(row):

            if slot == '-':
                continue

            left_diag_winner = diagWinCheck(board, rowNo, slotNo, slot, 'left')

            if left_diag_winner:
                return left_diag_winner

            right_diag_winner = diagWinCheck(board, rowNo, slotNo, slot, 'right')

            if right_diag_winner:
                return right_diag_winner

# If there's no winners, it must be a draw or still in progress
# Check there's no moves still to be made
    if any('-' in row for row in board):
        print("That is an unfinished board.")
        return 'in progress'
    else:
        print("It's a draw!")
        return 'draw'


def winCheck(matrix):
    # Establish winning sequences
    winning = ['YYYY','RRRR']

    # Check for winning sequence in each row
    for row in matrix:
        row_str = "".join(row)
        winner = [i for i in winning if i in row_str]

        if winner:
            print(f"Winner is {winner[0][0]}")
            return winner[0][0]
        else:
            continue
    
    return False


def diagWinCheck(board, rowNo, slotNo, colour, direction, count=1):

    if count == 4:
        print(f"Winner is {colour}")
        return colour

    # out of bounds check
    elif rowNo > 4:
        return False

    elif slotNo < 6 and direction is 'right' and board[rowNo + 1][slotNo + 1] == colour:
        rowNo += 1
        count += 1
        slotNo += 1
        return diagWinCheck(board, rowNo, slotNo, colour, direction, count)
    
    elif slotNo > 0 and direction is 'left' and board[rowNo + 1][slotNo - 1] == colour:
        rowNo += 1
        count += 1
        slotNo -= 1
        return diagWinCheck(board, rowNo, slotNo, colour, direction, count)

    return False

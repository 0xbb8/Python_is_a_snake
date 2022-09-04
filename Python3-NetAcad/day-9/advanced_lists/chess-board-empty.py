board = []
for i in range(8):
    row = ["a" for i in range(8)]
    board.append(row)
for i in range(8):print(board[i])
# This can also be written as following:
chess = [["." for i in range(8)] for i in range(8)]
print("board(nested list comprehension)")
for i in range(8):print(chess[i])
# List Comphresions can be nested. The chess and board in this program represents a 2D array of empty spaces of a chess board.

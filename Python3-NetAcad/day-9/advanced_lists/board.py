board=[]
for i in range(8):
    row = ["["+str(i)+"]"+"["+str(j)+"]" for j in range(8)]
    board.append(row)
# accessing the board. Putting pieces.
# using 2 indices.first row number, second field of the selected row (column no)
rook="Rook"
board[0][0]=rook
board[0][7]=rook
board[7][0]=rook
board[7][7]=rook
# printing the chess board.
print("Chess Board Array or Matrix")
for i in range(8):
    print(board[i])
    print()

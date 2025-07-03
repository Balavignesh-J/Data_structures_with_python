def is_safe(board,row,col):
    i=col
    while i>=0:
        if board[row][i]==1:
            return False
        i-=1

    i = col
    j = row
    while i >= 0 and j >= 0:
        if board[j][i] == 1:
            return False
        i -= 1
        j -= 1

    i = col
    j = row
    while i >= 0 and j <=row:
        if board[j][i] == 1:
            return False
        i -= 1
        j += 1

    return True

def backtrack(board,col,N):
    if col>=N:
        return True

    for row in range(N):
        if is_safe(board,row,col):
            board[row][col]=1

            if backtrack(board,col+1,N):
                return True

            board[row][col]=0

    return False



N=8
board=[[0 for k in range(N)] for k in range(N)]
solution = backtrack(board,0,N)

if solution:
    for i in range(N):
        for j in range(N):
            print(board[i][j],end=" ")
        print()
else:
    print("Can't able to place the queens")



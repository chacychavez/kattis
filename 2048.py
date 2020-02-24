board = []
size = 4
for i in range(size):
    str_input = input()
    board.append([int(s) for s in str_input.split(" ")])
direction = int(input())

if direction == 0: # left
    for i in range(size):
        for j in range(size):
            for k in range(j + 1, size):
                if board[i][k] == 0:
                    continue
                if board[i][j] == 0:
                    board[i][j] = board[i][k]
                    board[i][k] = 0
                elif board[i][j] == board[i][k]:
                    board[i][j] += board[i][k]
                    board[i][k] = 0
                    break
                else:
                    break
elif direction == 1: # up
    for j in range(size):
        for i in range(size):
            for k in range(i + 1, size):
                if board[k][j] == 0:
                    continue
                if board[i][j] == 0:
                    board[i][j] = board[k][j]
                    board[k][j] = 0
                elif board[i][j]  == board[k][j]:
                    board[i][j] += board[k][j]
                    board[k][j] = 0
                    break
                else:
                    break
elif direction == 2: # right
    for i in range(size):
        board[i] = list(reversed(board[i]))
        for j in range(size):
            for k in range(j + 1, size):
                if board[i][k] == 0:
                    continue
                if board[i][j] == 0:
                    board[i][j] = board[i][k]
                    board[i][k] = 0
                elif board[i][j]  == board[i][k]:
                    board[i][j] += board[i][k]
                    board[i][k] = 0
                    break
                else:
                    break
        board[i] = list(reversed(board[i]))
elif direction == 3: # down
    board = list(reversed(board))
    for j in range(size):
        for i in range(size):
            for k in range(i + 1, size):
                if board[k][j] == 0:
                    continue
                if board[i][j] == 0:
                    board[i][j] = board[k][j]
                    board[k][j] = 0
                elif board[i][j]  == board[k][j]:
                    board[i][j] += board[k][j]
                    board[k][j] = 0
                    break
                else:
                    break
    board = list(reversed(board))


for i in range(size):
    print(" ".join([str(n) for n in board[i]]))


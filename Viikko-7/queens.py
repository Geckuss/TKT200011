def count(n, k):
    board = [[0]*n for _ in range(n)]
    return dfs(board, 0, k)

def dfs(board, col, k):
    n = len(board)
    if k == 0:
        return 1
    if col == n:
        return 0
    count = 0
    for i in range(n):
        if is_valid(board, i, col):
            board[i][col] = 1
            count += dfs(board, col + 1, k - 1)
            board[i][col] = 0
    count += dfs(board, col + 1, k)
    return count

def is_valid(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, len(board)), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True
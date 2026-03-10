# Backtracking - N-Queen (BOJ 9663)

n = int(input())
answer = 0


def dfs(row, columns, diag_left, diag_right):
    global answer

    if row == n:
        answer += 1
        return

    available = ((1 << n) - 1) & ~(columns | diag_left | diag_right)

    while available:
        bit = available & -available
        available -= bit
        dfs(row + 1, columns | bit, (diag_left | bit) << 1, (diag_right | bit) >> 1)


dfs(0, 0, 0, 0)
print(answer)

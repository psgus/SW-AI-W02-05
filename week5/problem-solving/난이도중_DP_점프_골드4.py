# DP - Jump (BOJ 2253)

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
small_stones = {int(input()) for _ in range(m)}

if n == 1:
    print(0)
else:
    max_jump = int((2 * n) ** 0.5) + 3
    inf = 10 ** 9
    dp = [[inf] * (max_jump + 1) for _ in range(n + 1)]
    dp[1][0] = 0

    for stone in range(1, n + 1):
        if stone in small_stones:
            continue

        for jump in range(max_jump + 1):
            if dp[stone][jump] == inf:
                continue

            for next_jump in (jump - 1, jump, jump + 1):
                next_stone = stone + next_jump

                if next_jump <= 0 or next_jump > max_jump:
                    continue

                if next_stone <= n and next_stone not in small_stones:
                    dp[next_stone][next_jump] = min(dp[next_stone][next_jump], dp[stone][jump] + 1)

    result = min(dp[n])
    print(result if result != inf else -1)

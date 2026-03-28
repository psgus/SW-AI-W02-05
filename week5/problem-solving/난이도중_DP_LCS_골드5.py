# DP - LCS (BOJ 9251)

a = input().strip()
b = input().strip()
dp = [0] * (len(b) + 1)

for char_a in a:
    previous = 0

    for i, char_b in enumerate(b, start=1):
        temp = dp[i]

        if char_a == char_b:
            dp[i] = previous + 1
        else:
            dp[i] = max(dp[i], dp[i - 1])

        previous = temp

print(dp[-1])

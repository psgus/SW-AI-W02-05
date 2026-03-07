# Array - Above Average (BOJ 4344)

c = int(input())

for _ in range(c):
    data = list(map(int, input().split()))
    n = data[0]
    scores = data[1:]
    average = sum(scores) / n
    above = sum(score > average for score in scores)
    print(f"{above / n * 100:.3f}%")

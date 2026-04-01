# Greedy - New Recruits (BOJ 1946)

import sys

input = sys.stdin.readline

t = int(input())
answer = []

for _ in range(t):
    n = int(input())
    applicants = [tuple(map(int, input().split())) for _ in range(n)]
    applicants.sort()

    hired = 0
    best_interview = n + 1

    for _, interview_rank in applicants:
        if interview_rank < best_interview:
            hired += 1
            best_interview = interview_rank

    answer.append(str(hired))

print("\n".join(answer))

# Linked List - Railway Construction (BOJ 23309)

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
stations = list(map(int, input().split()))
max_station = 1_000_000
prev_station = [0] * (max_station + 1)
next_station = [0] * (max_station + 1)

for i in range(n):
    current = stations[i]
    prev_station[current] = stations[i - 1]
    next_station[current] = stations[(i + 1) % n]

answer = []

for _ in range(m):
    command = input().split()
    op = command[0]
    station = int(command[1])

    if op == "BN":
        new_station = int(command[2])
        old_next = next_station[station]
        answer.append(str(old_next))

        next_station[station] = new_station
        prev_station[new_station] = station
        next_station[new_station] = old_next
        prev_station[old_next] = new_station
    elif op == "BP":
        new_station = int(command[2])
        old_prev = prev_station[station]
        answer.append(str(old_prev))

        next_station[old_prev] = new_station
        prev_station[new_station] = old_prev
        next_station[new_station] = station
        prev_station[station] = new_station
    elif op == "CN":
        target = next_station[station]
        answer.append(str(target))

        after_target = next_station[target]
        next_station[station] = after_target
        prev_station[after_target] = station
    else:
        target = prev_station[station]
        answer.append(str(target))

        before_target = prev_station[target]
        prev_station[station] = before_target
        next_station[before_target] = station

print("\n".join(answer))

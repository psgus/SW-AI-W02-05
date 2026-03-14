# Stack - Stack (BOJ 10828)

import sys

input = sys.stdin.readline

n = int(input())
stack = []
answer = []

for _ in range(n):
    command = input().split()

    if command[0] == "push":
        stack.append(command[1])
    elif command[0] == "pop":
        answer.append(stack.pop() if stack else "-1")
    elif command[0] == "size":
        answer.append(str(len(stack)))
    elif command[0] == "empty":
        answer.append("0" if stack else "1")
    else:
        answer.append(stack[-1] if stack else "-1")

print("\n".join(answer))

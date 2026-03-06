# String - Repeating Characters (BOJ 2675)

t = int(input())

for _ in range(t):
    repeat, text = input().split()
    print("".join(char * int(repeat) for char in text))

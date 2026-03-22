# 분할정복 - 색종이 만들기 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/2630
n = int(input())
arr = []

for i in range(n):
    arr.append(list(map(int, input().split())))

white = 0
blue = 0

def divide(x, y, size):
    global white, blue
    color = arr[x][y]

    for i in range(x, x + size):
        for j in range(y, y + size):
            if arr[i][j] != color:
                half = size // 2

                divide(x, y, half)
                divide(x, y + half, half)
                divide(x + half, y, half)
                divide(x + half, y + half, half)

                return

    if color == 0:
        white += 1
    else:
        blue += 1


divide(0, 0, n)

print(white)
print(blue)
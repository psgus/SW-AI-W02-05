# Number Theory - Goldbach's Conjecture (BOJ 9020)

import sys

input = sys.stdin.readline

t = int(input())
numbers = [int(input()) for _ in range(t)]
limit = max(numbers)
is_prime = [True] * (limit + 1)
is_prime[0] = False
is_prime[1] = False

for number in range(2, int(limit ** 0.5) + 1):
    if is_prime[number]:
        for multiple in range(number * number, limit + 1, number):
            is_prime[multiple] = False

for number in numbers:
    for left in range(number // 2, 1, -1):
        right = number - left

        if is_prime[left] and is_prime[right]:
            print(left, right)
            break

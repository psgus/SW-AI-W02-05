# Hash Table - Minkyun's Password (BOJ 9933)

n = int(input())
words = [input().strip() for _ in range(n)]
word_set = set(words)

for word in words:
    if word[::-1] in word_set:
        print(len(word), word[len(word) // 2])
        break

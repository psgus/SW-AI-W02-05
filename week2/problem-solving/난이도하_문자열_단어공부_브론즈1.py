# String - Word Study (BOJ 1157)

word = input().strip().upper()
counts = [0] * 26

for char in word:
    counts[ord(char) - ord("A")] += 1

max_count = max(counts)

if counts.count(max_count) > 1:
    print("?")
else:
    print(chr(counts.index(max_count) + ord("A")))

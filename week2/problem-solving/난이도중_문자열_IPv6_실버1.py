# String - IPv6 (BOJ 3107)

address = input().strip()

if "::" in address:
    left, right = address.split("::")
    left_groups = left.split(":") if left else []
    right_groups = right.split(":") if right else []
    groups = left_groups + ["0"] * (8 - len(left_groups) - len(right_groups)) + right_groups
else:
    groups = address.split(":")

print(":".join(group.zfill(4) for group in groups))

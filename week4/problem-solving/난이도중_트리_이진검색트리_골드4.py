# Tree - Binary Search Tree (BOJ 5639)

import sys

sys.setrecursionlimit(100000)

preorder = list(map(int, sys.stdin.read().split()))
index = 0
postorder = []


def build_postorder(lower, upper):
    global index

    if index >= len(preorder):
        return

    value = preorder[index]

    if not (lower < value < upper):
        return

    index += 1
    build_postorder(lower, value)
    build_postorder(value, upper)
    postorder.append(value)


build_postorder(float("-inf"), float("inf"))
print("\n".join(map(str, postorder)))

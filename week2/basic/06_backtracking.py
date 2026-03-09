def combinations(n, k):
    result = []

    def backtrack(start, current_combination):
        if len(current_combination) == k:
            result.append(current_combination[:])
            return

        for number in range(start, n + 1):
            current_combination.append(number)
            backtrack(number + 1, current_combination)
            current_combination.pop()

    backtrack(1, [])
    return result


def combinations_itertools_compare(n, k):
    from itertools import combinations as comb

    return [list(c) for c in comb(range(1, n + 1), k)]


if __name__ == "__main__":
    print("=== 테스트 케이스 1 ===")
    n1, k1 = 4, 2
    result1 = combinations(n1, k1)
    print(f"C({n1}, {k1}) = {result1}")
    print(f"총 {len(result1)}개의 조합")
    print()

    print("=== 테스트 케이스 2 ===")
    n2, k2 = 5, 3
    result2 = combinations(n2, k2)
    print(f"C({n2}, {k2}) = {result2}")
    print(f"총 {len(result2)}개의 조합")
    print()

    print("=== 테스트 케이스 3 ===")
    n3, k3 = 3, 1
    result3 = combinations(n3, k3)
    print(f"C({n3}, {k3}) = {result3}")
    print(f"총 {len(result3)}개의 조합")
    print()

    print("=== 테스트 케이스 4 ===")
    n4, k4 = 4, 4
    result4 = combinations(n4, k4)
    print(f"C({n4}, {k4}) = {result4}")
    print(f"총 {len(result4)}개의 조합")

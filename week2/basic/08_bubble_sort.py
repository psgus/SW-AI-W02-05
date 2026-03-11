def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


def bubble_sort_optimized(arr):
    n = len(arr)

    for i in range(n - 1):
        swapped = False

        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

    return arr


if __name__ == "__main__":
    arr1 = [64, 34, 25, 12, 22, 11, 90]
    print("=== 테스트 케이스 1 ===")
    print(f"정렬 전: {arr1}")
    result1 = bubble_sort(arr1.copy())
    print(f"정렬 후: {result1}")
    print()

    arr2 = [1, 2, 3, 4, 5]
    print("=== 테스트 케이스 2: 이미 정렬됨 ===")
    print(f"정렬 전: {arr2}")
    result2 = bubble_sort_optimized(arr2.copy())
    print(f"정렬 후: {result2}")
    print("최적화 버전은 1번의 패스만 수행")
    print()

    arr3 = [5, 4, 3, 2, 1]
    print("=== 테스트 케이스 3: 역순 ===")
    print(f"정렬 전: {arr3}")
    result3 = bubble_sort(arr3.copy())
    print(f"정렬 후: {result3}")

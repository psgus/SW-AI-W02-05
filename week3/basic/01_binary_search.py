def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


if __name__ == "__main__":
    arr1 = [1, 3, 5, 7, 9, 11, 13]
    target1 = 7
    result1 = binary_search(arr1, target1)
    print(f"배열: {arr1}")
    print(f"찾는 값: {target1}")
    print(f"결과: 인덱스 {result1}")
    print()

    arr2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    target2 = 14
    result2 = binary_search(arr2, target2)
    print(f"배열: {arr2}")
    print(f"찾는 값: {target2}")
    print(f"결과: 인덱스 {result2}")
    print()

    arr3 = [1, 3, 5, 7, 9]
    target3 = 6
    result3 = binary_search(arr3, target3)
    print(f"배열: {arr3}")
    print(f"찾는 값: {target3}")
    print(f"결과: 인덱스 {result3}")

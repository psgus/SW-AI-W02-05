def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


def insertion_sort_with_steps(arr):
    print(f"초기 배열: {arr}")

    for i in range(1, len(arr)):
        key = arr[i]
        print(f"\nStep {i}: key = {key}")
        print(f"정렬된 부분: {arr[:i]}")

        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
        print(f"삽입 후: {arr}")

    return arr


if __name__ == "__main__":
    arr1 = [12, 11, 13, 5, 6]
    print("=== 테스트 케이스 1 ===")
    print(f"정렬 전: {arr1}")
    result1 = insertion_sort(arr1.copy())
    print(f"정렬 후: {result1}")
    print()

    arr2 = [5, 2, 4, 6, 1, 3]
    print("=== 테스트 케이스 2: 정렬 과정 ===")
    insertion_sort_with_steps(arr2.copy())
    print()

    arr3 = [1, 2, 3, 4, 5]
    print("=== 테스트 케이스 3: 이미 정렬됨 ===")
    print(f"정렬 전: {arr3}")
    result3 = insertion_sort(arr3.copy())
    print(f"정렬 후: {result3}")
    print("이미 정렬된 경우 O(n) 시간 소요")

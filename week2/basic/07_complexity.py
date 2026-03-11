def find_duplicates_brute_force(nums):
    duplicates = []

    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j] and nums[i] not in duplicates:
                duplicates.append(nums[i])

    return duplicates


def find_duplicates_sorting(nums):
    duplicates = []
    nums.sort()

    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1] and nums[i] not in duplicates:
            duplicates.append(nums[i])

    return duplicates


def find_duplicates_hash(nums):
    seen = set()
    duplicates = set()

    for num in nums:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)

    return list(duplicates)


def measure_time(func, nums, method_name):
    result = func(nums[:])
    print(f"{method_name}: {sorted(result)}")
    print()


if __name__ == "__main__":
    print("=== 테스트 케이스 1: 작은 배열 ===")
    nums1 = [4, 3, 2, 7, 8, 2, 3, 1]
    print(f"입력: {nums1}\n")

    result1 = find_duplicates_brute_force(nums1)
    print(f"방법1 (Brute Force): {sorted(result1)}")

    result2 = find_duplicates_sorting(nums1)
    print(f"방법2 (Sorting): {sorted(result2)}")

    result3 = find_duplicates_hash(nums1)
    print(f"방법3 (Hash): {sorted(result3)}")
    print()

    print("=== 테스트 케이스 2: 성능 비교 (n=1000) ===")
    import random

    random.seed(42)
    nums2 = [random.randint(1, 500) for _ in range(1000)]

    measure_time(find_duplicates_brute_force, nums2, "방법1 (O(n²))")
    measure_time(find_duplicates_sorting, nums2, "방법2 (O(n log n))")
    measure_time(find_duplicates_hash, nums2, "방법3 (O(n))")

    print("=== 복잡도 분석 요약 ===")
    print("방법1 - Brute Force:")
    print("  시간: O(n²), 공간: O(k)")
    print("  특징: 간단하지만 느림")
    print()
    print("방법2 - Sorting:")
    print("  시간: O(n log n), 공간: O(1)")
    print("  특징: 추가 메모리 없이 효율적")
    print()
    print("방법3 - Hash:")
    print("  시간: O(n), 공간: O(n)")
    print("  특징: 가장 빠르지만 메모리 사용")

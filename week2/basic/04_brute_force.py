def find_two_sum_pairs(nums, target):
    pairs = []

    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                pairs.append((i, j))

    return pairs


if __name__ == "__main__":
    nums1 = [2, 7, 11, 15]
    target1 = 9
    result1 = find_two_sum_pairs(nums1, target1)
    print(f"배열: {nums1}")
    print(f"목표 합: {target1}")
    print(f"결과 쌍: {result1}")
    print()

    nums2 = [1, 3, 4, 2, 5, 6]
    target2 = 7
    result2 = find_two_sum_pairs(nums2, target2)
    print(f"배열: {nums2}")
    print(f"목표 합: {target2}")
    print(f"결과 쌍: {result2}")
    print()

    nums3 = [1, 1, 1, 1]
    target3 = 2
    result3 = find_two_sum_pairs(nums3, target3)
    print(f"배열: {nums3}")
    print(f"목표 합: {target3}")
    print(f"결과 쌍: {result3}")

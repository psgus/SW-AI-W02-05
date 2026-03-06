def is_palindrome(s):
    normalized = "".join(char.lower() for char in s if char.isalnum())
    return normalized == normalized[::-1]


if __name__ == "__main__":
    test1 = "A man, a plan, a canal: Panama"
    result1 = is_palindrome(test1)
    print(f'입력: "{test1}"')
    print(f"회문 여부: {result1}")
    print()

    test2 = "race a car"
    result2 = is_palindrome(test2)
    print(f'입력: "{test2}" raca')
    print(f"회문 여부: {result2}")
    print()

    test3 = "Was it a car or a cat I saw?"
    result3 = is_palindrome(test3)
    print(f'입력: "{test3}"')
    print(f"회문 여부: {result3}")
    print()

    test4 = "Madam"
    result4 = is_palindrome(test4)
    print(f'입력: "{test4}"')
    print(f"회문 여부: {result4}")

# Number Theory - Finding Prime Numbers (BOJ 1978)

n = int(input())
numbers = list(map(int, input().split()))


def is_prime(number):
    if number < 2:
        return False

    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False

    return True


print(sum(is_prime(number) for number in numbers))

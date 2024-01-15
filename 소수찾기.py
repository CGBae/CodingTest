from itertools import permutations

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    unique_numbers = set()

    for i in range(1, len(numbers) + 1):
        perms = permutations(numbers, i)
        for perm in perms:
            unique_numbers.add(int(''.join(perm)))

    for num in unique_numbers:
        if is_prime(num):
            answer += 1

    return answer
def solution(numbers):
    compare_func = lambda x: (x * 4)[:10]

    sorted_numbers = sorted(map(str, numbers), key=compare_func, reverse=True)

    if sorted_numbers[0] == '0':
        return '0'

    return ''.join(sorted_numbers)

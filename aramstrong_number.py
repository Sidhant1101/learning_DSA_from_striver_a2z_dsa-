def aramstrong_number(num):
    original_num = num
    cube_sum = 0

    while num > 0:
        digit = num % 10
        cube_sum += digit ** 3
        num = num // 10

    return cube_sum == original_num

print(aramstrong_number(371))  # prints True
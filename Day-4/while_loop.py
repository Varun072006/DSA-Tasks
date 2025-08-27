def sum_of_digits(num):
    total = 0
    while num > 0:
        digit = num % 10
        total += digit
        num //= 10
    return total

num = 1234
print("Sum of digits:", sum_of_digits(num))
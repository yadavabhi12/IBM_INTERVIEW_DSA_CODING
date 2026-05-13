# method 1 brute force method
def add_digits(num):
    while num >= 10:
        sum = 0
        while num > 0:
            sum += num % 10
            num //= 10
        num = sum
    return num


# optimal method
def add_digits_optimal(num):
    return (num - 1) % 9 + 1 if num != 0 else 0
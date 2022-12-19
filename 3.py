# Soru 3.
def is_palindrome(n):
    return str(n) == str(n)[::-1]

largest_number = 0
for i in range(999, 100, -1):
    for j in range(999, 100, -1):
        result = i * j
        if is_palindrome(result) and result > largest_number:
            largest_number = result

print(largest_number)

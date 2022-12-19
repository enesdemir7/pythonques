# Soru 4.
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

counter = 0
current = 2

while counter < 10001:
    if is_prime(current):
        counter += 1
    current += 1

print(current - 1)

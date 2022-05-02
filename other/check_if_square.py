def is_square(n):
    if n >= 0:
        print(n ** 0.5, (n ** 0.5) ** 2)
        return (n ** 0.5) ** 2 == n
    return False


print(is_square(1))
print(is_square(2))
print(is_square(3))
print(is_square(4))
print(is_square(5))
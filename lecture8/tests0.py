from prime import is_prime


def test_prime(n, expected):
    if is_prime(n) != expected:
        print(f"ERROR on is_prime({n}), expected {expected}")


if __name__ == "__main__":
    test_prime(-4, False)
    test_prime(-3, False)
    test_prime(-2, False)
    test_prime(-1, False)
    test_prime(0, False)
    test_prime(1, False)
    test_prime(2, True)
    test_prime(3, True)
    test_prime(4, False)

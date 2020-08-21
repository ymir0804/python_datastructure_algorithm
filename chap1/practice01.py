def convert_to_decimal(num, base):
    multiplier, result = 1, 0
    while num > 0:
        result += num % 10 * multiplier
        multiplier *= base
        num = num // 10
    return result


def test_convert_to_decimal():
    num, base = 1001, 2
    assert (convert_to_decimal(num, base) == 9)
    print('테스트 통과')


def convert_from_decimal(decimal, base):
    multiplier, result = 1, 0
    while decimal > 0:
        result += decimal % base * multiplier
        multiplier *= 10
        decimal = decimal // base
    return result


def test_convert_from_decimal():
    num, base = 9, 2
    assert (convert_from_decimal(num, base) == 1001)
    print('테스트 통과')


if __name__ == "__main__":
    test_convert_to_decimal()
    test_convert_from_decimal()

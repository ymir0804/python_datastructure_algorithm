def convert_from_decimal_larger_bases(num, base):
    strings = '0123456789ABCDEFGHIJ'
    result = ""
    while num > 0:
        # 해당 인덱스 참조
        digit = num % base
        # 1F 인 경우 처음에 result 에 F가 들어가고 그 다음에 1이들어가서 1+F -> 1F 출력
        result = strings[digit] + result
        num = num // base
    return result


def test_convert_from_decimal_larger_bases():
    num, base = 31, 16
    assert(convert_from_decimal_larger_bases(num, base) == "1F")
    print("테스트 통과")


if __name__ == '__main__':
    test_convert_from_decimal_larger_bases()
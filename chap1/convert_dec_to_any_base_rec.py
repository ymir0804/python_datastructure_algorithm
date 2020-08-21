def convert_dec_to_any_base_rec(num, base):
    convertString = "0123456789ABCDEF"
    if num < base:
        # 진수를 계산할 숫자가 20안에 있는 경우 그냥 해당 숫자를 리턴
        return convertString[num]
    else:
        return convert_dec_to_any_base_rec(num // base, base) + convertString[num % base]


def test_convert_dec_to_any_base_rec():
    num = 9
    base = 2
    assert(convert_dec_to_any_base_rec(num, base) == '1001')
    print('테스트 통과')


if __name__ == '__main__':
    test_convert_dec_to_any_base_rec()
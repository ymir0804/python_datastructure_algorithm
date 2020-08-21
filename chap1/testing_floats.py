# equality test
def equality_test(test_num1, test_num2, places=7):
    return round(abs(test_num1 - test_num2), places) == 0


from fractions import Fraction


# fraction module

def rounding_floats(number1, places):
    return round(number1, places)


def float_to_fractions(number):
    return Fraction(*number.as_interger_ratio())


def get_denominator(num1, num2):
    # 분모반환
    a = Fraction(num1, num2)
    return a.denominator


def get_numerator(num1, num2):
    # 분자반환
    a = Fraction(num1, num2)
    return a.numerator


def test_floats():
    num1 = 1.25
    num2 = 1
    num3 = -1
    num4 = 5/4
    num6 = 6
    # assert 함수를 이용하여 참과 거짓을 판별
    assert(rounding_floats(num1, num2) == 1.2)
    assert(rounding_floats(num1 * 10, num3) == 10)
    assert(float_to_fractions(num1) == num4)
    assert(get_denominator(num2,num6) == num6)
    assert(get_numerator(num2,num6) == num2)
    print('테스트 통과')


if __name__ == "__main__":
    test_testing_floats()
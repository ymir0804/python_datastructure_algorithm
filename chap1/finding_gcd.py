# Using While
def finding_gcd_loop(a, b):
    while b != 0 :
        result = b
        a, b = b, a % b
    return result


# Using recursive function
def finding_gcd_rec(a,b):
    if b == 0:
        return a
    else:
        return finding_gcd_rec(b, a % b)


def test_finding_gcd_loop():
    num1 = 21
    num2 = 12
    assert(finding_gcd_loop(num1, num2) == 3)
    print('테스트 통과')


def test_finding_gcd_rec():
    num1 = 21
    num2 = 12
    assert(finding_gcd_rec(num1, num2) == 3)
    print('테스트 통과')


if __name__ == "__main__":
    test_finding_gcd_loop()
    test_finding_gcd_rec()
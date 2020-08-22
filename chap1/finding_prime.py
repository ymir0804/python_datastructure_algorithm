import math
import random


# brute_force 를 이용하여 소수를 찾는방법 -> 시간 복잡도에서 비효율적인 것 같음
def finding_prime(number):
    num = abs(number)
    if num < 4:
        return True
    for x in range(2, num):
        if number % x == 0:
            return False
    return True


# 제곱근을 이용하여 소수를 찾는 방법
'''
만약에 내가 찾을 소수가 11이라면 range 에 int(√11) + 1값이 4이므로 
x에 2,3 값이 들어간다 
11 % 2 != 0 && 11 % 3 != 0 이므로 소수이다. 
'''


def finding_prime_sqrt(number):
    num = abs(number)
    if num < 4:
        return True
    for x in range(2, int(math.sqrt(num)) + 1):
        if number % x == 0:
            return False
    return True


# 페르마의 소정리를 사용하여 해결
'''
페르마의 소정리란 어떤 수가 소수일 간단한 필요조건 
p가 소수이고 a가 p의 배수가 아니면 a^p-1을 p로 나눈 나머지는 1
'''


def finding_prime_fermat(number):
    if number <= 102:
        for a in range(2, number):
            if pow(a, number-1, number) != 1:
                return False
        return True
    else:
        for i in range(100):
            a = random.randint(2, number - 1)
            if pow(a, number -1, number) != 1:
                return False
        return True


def test_finding_prime():
    number1 = 17
    number2 = 20
    assert(finding_prime(number1) is True)
    assert(finding_prime(number2) is False)
    assert(finding_prime_sqrt(number1) is True)
    assert(finding_prime_sqrt(number2) is False)
    assert(finding_prime_fermat(number1) is True)
    assert(finding_prime_fermat(number2) is False)
    print('테스트 통과')


if __name__ == "__main__":
    test_finding_prime()
import math
import random
import sys


def finding_prime_sqrt(number):
    num = abs(number)
    if num < 4:
        return True
    for x in range(2, int(math.sqrt(num)) + 1):
        if number % x == 0:
            return False
        return True


def generate_prime(number=3):
    while 1:
        # n 비트 값 생성 과정
        p = random.randint(pow(2, number - 2), pow(2, number - 1) - 1)
        # 생성된 n 비트의 값을 소수로 변환하는 과정
        p = (2 * p) + 1
        if finding_prime_sqrt(p):
            return p


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: generate_prime.py number")
        sys.exit()
    else:
        # 첫번째 매개변수를 넘겨주는 과정
        number = int(sys.argv[1])
        # 3을 대입하게 되면 3비트 소수 값을 생성합니다. 3비트값은 4~7까지 있으므로, 5,7 값이 출력됩니다.
        print(generate_prime(number))
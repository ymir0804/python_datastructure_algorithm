import random


def testing_random():
    # Random Module test
    values = [1, 2, 3, 4]
    print(random.choice(values))
    print(random.choice(values))
    print(random.choice(values))
    # Sample 메소드는 정수를 인자로 받아서 인자로 받은 정수 만큼 리턴
    print(random.sample(values, 2))
    print(random.sample(values, 3))

    # 리스트 섞기
    random.shuffle(values)
    print(values)

    # 0 ~ 10 사이의 정수 리턴
    print(random.randint(0, 10))
    print(random.randint(0, 10))


if __name__ == "__main__":
    testing_random()
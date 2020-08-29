class Symbol(object):
    def __init__(self, value):
        self.value = value


if __name__ == '__main__':
    x = Symbol("Py")
    y = Symbol("Py")

    symbols = set()
    symbols.add(x)
    symbols.add(y)

    # x 객체와 y 객체가 같은지 출력
    print(x is y)
    # x 객체의 value 와 y 객체의 value 가 같은지 출력 True 가 나와야합니다.
    print(x == y)
    print(len(symbols))
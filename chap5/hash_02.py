class Symbol(object):
    # 초기화를 위한 __init__ 메소드 선언
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return self.value == other.value
        else:
            return NotImplemented

    def __hash__(self):
        return hash(self.value)


if __name__ == '__main__':
    x = Symbol("Py")
    y = Symbol("Py")

    symbols = set()
    symbols.append(x)
    symbols.append(y)

    print(x is y)
    print(x == y)
    print(len(symbols))
    # 이경우 unhashable type 이라는 결과가 나오는데 가변 객체임을 의미 set 자료형은 불변 객체이므로 새로운 메소드를 추가시켜 해결해야함
    # 기본적으로 파이썬에서 사용자 정의 클래스의 모든 객체는 hashable 합니다. 이 뜻은, 불변 객체이고, hash()속성을 호출할 수 있다는 뜻입니다.

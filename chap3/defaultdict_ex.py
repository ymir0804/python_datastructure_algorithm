from collections import defaultdict


def default_dict_ex():
    pairs = {("a", 1), ("b", 2), ("c", 3)}

    # 일반적인 딕셔너리
    d1 = {}
    for key, value in pairs:
        # 누락된 키 처리
        if key not in d1:
            d1[key] = []
        d1[key].append(value)
    print(d1)

    # default_dict
    d2 = defaultdict(list)
    # item 의 타입이 list 인 dict 생성
    for key, value in pairs:
        d2[key].append(value)
    print(d2)


if __name__ == '__main__':
    default_dict_ex()
from collections import OrderedDict

# 삽입 순서대로 항목 저장


def ordered_dict_ex():
    pairs = [("c", 1), ("b", 2), ("a", 3)]
    d1 = {}

    for key, value in pairs:
        if key not in d1:
            d1[key] = []
        d1[key].append(value)
    for key in d1:
        print(key, d1[key])

    d2 = OrderedDict(pairs)
    for key in d2:
        print(key, d2[key])


if __name__ == '__main__':
    ordered_dict_ex()

import itertools

# 재귀를 이용하여 순열 구현
def perm(main_string):
    if len(main_string) < 2:
        return main_string
    res = []
    for i, c in enumerate(main_string):
        for cc in perm(main_string[:i] + main_string[i+1:]):
            res.append(c + cc)
    return res


# itertools 모듈을 이용하여 순열 사용
def perm2(main_string):
    res = itertools.permutations(main_string)
    return ["".join(i) for i in res]


if __name__ == '__main__':
    val = "012"
    print(perm(val))
    print(perm2(val))

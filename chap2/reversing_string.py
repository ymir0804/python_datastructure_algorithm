
# 재귀함수를 이용한 변환 방법
def revert_rec(s):
    if s:
        s = s[-1] + revert_rec(s[:-1])
    return s


# 일밙거인 문자열 전체 반환
def revert2(string):
    return string[::-1]


if __name__ == "__main__":
    str1 = '안녕 세상!'
    str2 = revert_rec(str1)
    str3 = revert2(str1)
    print(str2)
    print(str3)
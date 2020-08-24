def is_palindrome(s):
    # l 변수에 s를 공백으로 기준하여 나누고 s2로 다시 합친뒤 슬라이스를 역순으로 참조하여 찾는 방법
    l = s.split(" ")
    s2 = "".join(l)
    return s2 == s2[::-1]


def is_palindrome2(s):
    l = len(s)
    # 더블 포인터를 사용하여 해결
    f, b = 0, l - 1
    while f < l // 2:
        while s[f] == " ":
            f += 1
        while s[b] == " ":
            b -= 1
        if s[f] != s[b]:
            return False
        f += 1
        b -= 1
    return True


def is_palindrome3(s):
    s = s.strip()
    if len(s) < 2:
        return True
    if s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    else:
        return False


if __name__ == '__main__':
    str1 = "다시 합창합시다"
    str2 = ""
    str3 = "hello"
    print(is_palindrome(str1))
    print(is_palindrome(str2))
    print(is_palindrome(str3))
    print()
    print(is_palindrome2(str1))
    print(is_palindrome2(str2))
    print(is_palindrome2(str3))
    print()
    print(is_palindrome3(str1))
    print(is_palindrome3(str2))
    print(is_palindrome3(str3))


from collections import Counter
import string


def is_anagram(s1, s2):
    counter = Counter()
    # 첫번째 매개변수로 받은 문자열을 쪼개서 key, item 으로 구분 후 item 의 갯수 세기
    for c in s1:
        counter[c] += 1
    # 두번째 매개변수로 받은 문자열을 쪼개서 key, item 으로 구분 후 해당 key 가 있는 경우 item 갯수 제거
    for c in s2:
        counter[c] -= 1

    for i in counter.values():
        # 만약에 매개변수로 받은 문자열들이 애너그램이 아닌경우, 딕셔너리에 값이 존재하기 때문에 True가 들어갑니다.
        if i:
            return False
        return True


def hash_func(astring):
    s = 0
    for one in astring:
        if one in string.whitespace:
            continue
        s += ord(one)
    return s


def find_anagram_hash_function(word1, word2):
    return hash_func(word1) == hash_func(word2)


def test_find_anagram_hash_function():
    word1 = "buffy"
    word2 = "bffyu"
    word3 = "bffya"
    assert(find_anagram_hash_function(word1, word2) is True)
    assert(find_anagram_hash_function(word2, word3) is False)
    print('테스트 통과')


if __name__ == '__main__':
    test_find_anagram_hash_function()
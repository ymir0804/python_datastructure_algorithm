import string


def delete_unique_word(str1):
    # key 값에 char 을 key 로 두고 소문자로 대입
    table_c = {key: 0 for key in string.ascii_lowercase}
    for i in str1:
        table_c[i] += 1
    for key, value in table_c.items():
        # 중복되는 단어 처리
        if value > 1:
            str1 = str1.replace(key, "")
    return str1


def test_delete_unique_word():
    str1 = "google"
    assert(delete_unique_word(str1) == "le")
    print('테스트 통과!')


if __name__ == '__main__':
    test_delete_unique_word()
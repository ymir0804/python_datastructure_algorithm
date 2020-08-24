def reverser(main_string, p1=0, p2=None):
    # 단어의 길이는 무조건 2글자 이상이므로 2미만인 경우 그대로 리턴
    if len(main_string) < 2:
        return main_string
    p2 = p2 or len(main_string)-1

    # 문자열 문자 단위로 반환
    while p1 < p2:
        main_string[p1], main_string[p2] = main_string[p2], main_string[p1]
        p1 += 1
        p2 -= 1


def reversing_words_sentence_logic(main_string):
    reverser(main_string)
    string_index = 0
    start_index = 0
    while string_index < len(main_string):
        # 띄어쓰기가 있는 경우 문자열 변환
        if main_string[string_index] == " ":
            reverser(main_string, start_index, string_index-1)
            start_index = string_index + 1
        string_index += 1
    reverser(main_string, start_index, string_index-1)
    return "".join(main_string)

def reverse_wrod_brute(main_string):
    words,


if __name__ == '__main__':
    str1 = "파이썬 알고리즘 정말 재미있다."
    str2 = reversing_words_sentence_logic(list(str1))
    print(str2)



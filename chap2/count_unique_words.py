import string
import sys


def count_unique_word():
    words = {}
    strip = string.whitespace + string.punctuation + string.digits + "\"'"
    # 첫번째 매개변수부터 끝까지  filename 변수에 집어 넣음
    for filename in sys.argv[1:]:
        # 매개변수명 파일을 열기
        with open(filename) as file:
            # line 변수에 수행할 파일 대입
            for line in file:
                # word 변수에는 line 파일 코드의 단어들을 소문자로 구분
                for word in line.lower().split():
                    # word 변수에 whitespace, punctuation, digits, \로 구분한 단어들을 대입
                    word = word.strip(strip)
                    # 단어 구분 if문
                    if len(word) > 2:
                        # 단어가 처음 등장하는 경우 0 + 1을 이용하여 갯수 대입
                        words[word] = words.get(word, 0) + 1
    # 출연한 단어 및 갯수 출력
    for word in sorted(words):
        print("{0}: {1}번".format(word, words[word]))


if __name__ == "__main__":
    count_unique_word()

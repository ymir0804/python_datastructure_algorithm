from collections import Counter


def find_top_n_recurring_words(seq, n):
    word_counter = Counter()
    for word in seq.split():
        word_counter[word] += 1
    return word_counter.most_common(n)


def test_find_top_n_recurring_words():
    seq = "버피 에인절 몬스터 잰더 윌로 버피 몬스터 슈퍼 버피 에인절"
    n = 3
    '''most_common 메소드 key, value로 리턴 '''
    assert (find_top_n_recurring_words(seq, n) == [("버피", 3), ("에인절", 2), ("몬스터", 2)])
    print('테스트통과!')


if __name__ == '__main__':
    test_find_top_n_recurring_words()
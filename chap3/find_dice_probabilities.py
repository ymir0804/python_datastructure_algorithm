from collections import Counter, defaultdict


def find_dice_probabilities(s, n_faces=6):
    if s > 2 * n_faces or s < 2:
        return None

    c_dict = Counter()
    d_dict = defaultdict(list)

    # 1,1 ~ 6,6 까지 모두 대입
    for dice1 in range(1, n_faces+1):
        for dice2 in range(1, n_faces+1):
            t = [dice1, dice2]
            c_dict[dice1 + dice2] += 1
            d_dict[dice1 + dice2].append(t)
    return [c_dict[s], d_dict[s]]


def test_find_dice_probabilities():
    n_faces = 6
    s = 5
    results = find_dice_probabilities(s, n_faces)
    print(results)
    assert(results[0] == len(results[1]))
    print('테스트 통과!')


if __name__ == '__main__':
    test_find_dice_probabilities()
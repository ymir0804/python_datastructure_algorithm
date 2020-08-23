import numpy as np


def testing_numpy():
    '''tests many features of numpy'''

    ax = np.array([1, 2, 3])
    ay = np.array([3, 4, 5])
    print(ax)
    print(ay)
    # 배열값에 두배를 하여 계산 2, 4, 6
    print(ax * 2)
    # 배열값에 더하기 연산
    print(ax + 10)
    # 배열값에 있는 값들의 제곱근으로 바꿔 계산
    print(np.sqrt(ax))
    # 배열값에 있는 값들의 코사인 계산 Ex) cos(1), cos(2), cos(3)
    print(np.cos(ax))

    print(ax - ay)
    print(np.where(ax < 2, ax , 10))
    m = np.matrix([ax, ay, ax])
    print(m)
    print(m.T)

    grid1 = np.zeros(shape=(10,10), dtype=float)
    grid2 = np.ones(shape=(10, 10), dtype=float)
    print(grid1)
    print(grid2)
    print(grid1[1] + 10)
    print(grid2[:,2] * 2)


if __name__ == "__main__":
    testing_numpy()
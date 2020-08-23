import numpy
import time


def trad_version():
    t1 = time.time()
    X = range(10000000)
    Y = range(10000000)
    Z = []
    for i in range(len(X)):
        Z.append(X[i] + Y[i])
    return time.time() - t1


def numpy_version():
    t1 = time.time()
    X = numpy.arange(10000000)
    Y = numpy.arange(10000000)
    Z = X + Y
    return time.time() - t1


if __name__ == "__main__":
    print(trad_version())
    print(numpy_version())

# numpy 배열이 파이썬 리스트보다 훨씬 더 효율적!

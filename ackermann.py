# coding=utf-8

__author__ = "amfox"

import sys

calls = 0


def naive_ackermann(m, n):
    global calls
    calls += 1
    if m == 0:
        return n + 1
    elif n == 0:
        return naive_ackermann(m - 1, 1)
    else:
        return naive_ackermann(m - 1, naive_ackermann(m, n - 1))


def iterative_ackermann(m, n):
    global calls
    calls += 1
    while m != 0:
        if n == 0:
            n = 1
        else:
            n = iterative_ackermann(m, n - 1)
        m -= 1
    return n + 1


def formula_ackermann(m, n):
    global calls
    calls += 1
    while m >= 4:
        if n == 0:
            n = 1
        else:
            n = formula_ackermann(m, n - 1)
        m -= 1
    if m == 3:
        return (1 << n + 3) - 3
    elif m == 2:
        return (n << 1) + 3
    elif m == 1:
        return n + 2
    else:  # m == 0
        return n + 1


if __name__ == "__main__":
    m = long(sys.argv[1])
    n = long(sys.argv[2])

    calls = 0
    result = naive_ackermann(m, n)
    print "Naive:     %d (%d calls)" % (result, calls)

    calls = 0
    result = iterative_ackermann(m, n)
    print "Iterative: %d (%d calls)" % (result, calls)

    calls = 0
    result = formula_ackermann(m, n)
    print "Formula:   %d (%d calls)" % (result, calls)

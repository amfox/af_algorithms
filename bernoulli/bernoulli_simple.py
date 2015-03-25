# coding=utf-8

__author__ = "amfox"

from gmpy import mpq, bincoef as _bincoef


def bincoef(n, k):
    if k < 0:
        return 0
    else:
        return _bincoef(n, k)


class memo:
    def __init__(self, f):
        self.func = f
        self.cache = {}
        self.highest = 0

    def __call__(self, m):
        if m < self.highest:
            return self.cache[m]
        else:
            x = self.func(m)
            self.cache[m] = x
            self.highest = m
            return x


@memo
def bernoulli(m):
    if m == 0: return 1
    if m == 1: return -mpq(1, 2)
    if m % 2: return 0
    s = 0
    for j in range(0, m):
        s += bincoef(m + 1, j) * bernoulli(j)
    b = -mpq(s) / bincoef(m + 1, m)
    return b

# coding=utf-8

__author__ = "amfox"


def mvmul(matrix, vector):
    return map(lambda m: sum(map(lambda u, v: u * v, m, vector)), matrix)

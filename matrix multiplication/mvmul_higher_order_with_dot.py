# coding=utf-8
from numpy.oldnumeric.ma import dot

__author__ = "amfox"


def mvmul(matrix, vector):
    return map(lambda m: dot(m, vector), matrix)

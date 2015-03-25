# coding=utf-8
from numpy.oldnumeric.ma import dot

__author__ = "amfox"


def mvmul(matrix, vector):
    return [dot(m, vector) for m in matrix]

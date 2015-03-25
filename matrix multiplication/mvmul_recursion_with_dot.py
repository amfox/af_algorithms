# coding=utf-8
from numpy.oldnumeric.ma import dot

__author__ = "amfox"


def mvmul(matrix, vector):
    if matrix:
        return [dot(matrix[0], vector)] + \
               mvmul(matrix[1:], vector)
    else:
        return []


# coding=utf-8

__author__ = "amfox"


def vadd(vector1, vector2):
    newVector = []
    for (v1, v2) in zip(vector1, vector2):
        newVector.append(v1 + v2)
    return newVector


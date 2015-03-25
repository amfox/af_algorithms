# coding=utf-8

__author__ = "amfox"


def vadd(vector1, vector2):
    for i, (v1, v2) in enumerate(zip(vector1, vector2)):
        vector1[i] = v1 + v2
    return vector1

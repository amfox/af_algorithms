# coding=utf-8

__author__ = "amfox"


def vadd(vector1, vector2):
    if vector1 and vector2:
        return [vector1[0] + vector2[0]] + vadd(vector1[1:], vector2[1:])
    else:
        return []

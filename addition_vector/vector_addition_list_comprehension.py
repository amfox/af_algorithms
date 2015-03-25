# coding=utf-8

__author__ = "amfox"


def vadd(vector1, vector2):
    return [v1 + v2 for (v1, v2) in zip(vector1, vector2)]

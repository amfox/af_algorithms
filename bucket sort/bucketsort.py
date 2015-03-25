# coding=utf-8

__author__ = "amfox"


def bucketSort(arr):
    count = [0] * len(arr)
    for value in arr:
        count[value] += 1
    arr = []
    for nr, amount in enumerate(count):
        arr.extend([nr] * amount)
    return arr


arr = [1, 3, 4, 6, 4, 2, 9, 1, 2, 9]

for val in arr:
    print val,
print

arr = bucketSort(arr)

for val in arr:
    print val,
print

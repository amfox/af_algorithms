# coding=utf-8

__author__ = "amfox"


def encode(cs):
    d, w = {0: ''}, 0
    dodict = lambda d, k: d.get(k) or d.__setitem__(k, len(d)) or 0
    return [tok for c in cs for tok in [(w, c)]
            for w in [dodict(d, tok)] if not w] + [(w, '')]


def decode(ts):
    d, j = {0: ''}, ''.join
    dodict = lambda d, v: d.__setitem__(len(d), v) or v
    return j([dodict(d, d[w] + c) for (w, c) in ts])


if __name__ == '__main__':
    test = "wow! how now brown plow cow"
    print encode(test)
    print decode(encode(test))

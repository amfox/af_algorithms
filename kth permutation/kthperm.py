# coding=utf-8

__author__ = "amfox"

rr = lambda n, k: (n > 1) and [k % n] + rr(n - 1, k / n) or [0]

dfr = lambda rs: len(rs) and rs[:1] + [r + (rs[0] <= r) for r in dfr(rs[1:])] or []

par = lambda rs: sum(rs) % 2

perm = lambda xs, k: [xs[i] for i in dfr(rr(len(xs), k))]

if __name__ == "__main__":
    for k in range(24):
        print "".join(perm("perm", k)), par(rr(4, k))

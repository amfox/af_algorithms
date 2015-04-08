from decimal import *

def exp(x):
    getcontext().prec += 3
    if x < 0:
        s = 1 / exp(abs(x))
    else:
        xpower = 1
        ns = 0
        s = 1
        n = 0
        factorial = 1
        while s != ns:
            s = ns
            term = Decimal(xpower) / factorial
            ns = s + term
            xpower *= x
            n += 1
            factorial *= n
    getcontext().prec -= 3
    return +s

def test_exp():
    assert exp(4) == +Decimal("54.59815003314423907811026120286")
    assert exp(0) == 1
    assert exp(-8) == +Decimal("0.0003354626279025118388213891257809")
    assert exp(Decimal("0.6931471805599453094172321214582")) == 2

from math import log as _flog

def log(x):
    if x < 0:
        return Decimal("NaN")
    if x == 0:
        return Decimal("-inf")
    getcontext().prec += 3
    eps = Decimal("10")**(-getcontext().prec+2)
    # A good initial estimate is needed
    r = Decimal(repr(_flog(float(x))))
    while 1:
        r2 = r - 1 + x/exp(r)
        if abs(r2-r) < eps:
            break
        else:
            r = r2
    getcontext().prec -= 3
    return +r
def test_log():
    A = [4, 1, Decimal("0.67753892")]
    for p in [5, 40, 28]:
        getcontext().prec = p
        eps = Decimal("10")**(-getcontext().prec + 2)
        for a in A:
            w = exp(log(a))
            assert abs(w - a) < eps

if __name__ == "__main__":
    test_exp()
    test_log()


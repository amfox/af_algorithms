# coding=utf-8

__author__ = "amfox"

from bernoulli_simple import bernoulli as bernoulli1
from bernoulli_faster import bernoulli as bernoulli2
from bernoulli_faster_yet import bernoulli as bernoulli3
from time import clock

for i in range(50):
    assert bernoulli1(i) == bernoulli2(i) == bernoulli3(i)

a = clock()
temp = bernoulli1(1000)
print "simple:", clock() - a, "seconds"

a = clock()
temp = bernoulli2(1000)
print "faster:", clock() - a, "seconds"

a = clock()
temp = bernoulli3(1000)
print "faster yet:", clock() - a, "seconds"


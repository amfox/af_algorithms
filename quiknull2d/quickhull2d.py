#coding=utf-8
from numpy import *

link = lambda a,b: concatenate((a,b[1:]))
edge = lambda a,b: concatenate(([a],[b]))
def qhull(sample):
    def dome(sample,base): 
        h, t = base
        dists = dot(sample-h, dot(((0,-1),(1,0)),(t-h)))
        outer = repeat(sample, dists>0, 0)

        if len(outer):
            pivot = sample[argmax(dists)]
            return link(dome(outer, edge(h, pivot)),
                        dome(outer, edge(pivot, t)))
        else:
            return base
    if len(sample) > 2:
    	axis = sample[:,0]
    	base = take(sample, [argmin(axis), argmax(axis)], 0)
    	return link(dome(sample, base),
                    dome(sample, base[::-1]))
    else:
	return sample

if __name__ == "__main__":
    #sample = 10*array([(x,y) for x in arange(10) for y in arange(10)])
    sample = 100*random.random((32,2))
    hull = qhull(sample)
	
    print "%!"
    print "100 500 translate 2 2 scale 0 0 moveto"
    print "/tick {moveto 0 2 rlineto 0 -4 rlineto 0 2 rlineto"
    print "              2 0 rlineto -4 0 rlineto 2 0 rlineto} def"
    for (x,y) in sample:
	print x, y, "tick"
    print "stroke"
    print hull[0,0], hull[0,1], "moveto"
    for (x,y) in hull[1:]:
	print x, y, "lineto"
    print "closepath stroke showpage"

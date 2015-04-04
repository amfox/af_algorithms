# The authors of this work have released all rights to it and placed it
# in the public domain under the Creative Commons CC0 1.0 waiver
# (http://creativecommons.org/publicdomain/zero/1.0/).
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# 
# Retrieved from: http://en.literateprograms.org/Parallel_prefix_(Python)?oldid=16590

from itertools import imap
vect = imap

def scan(op,a):
        print a
        if len(a) > 1:
                a[1::2] = vect(op,a[0::2],a[1::2])
                a[1::2] = scan(op,a[1::2])
                a[2::2] = vect(op,a[1::2],a[2::2])
        print a
        return a
def segmented_sum(xps,yps):
        x,xf = xps
        y,yf = yps
        if yf:  return (  y,yf)
        else:   return (x+y,xf)
if __name__ == "__main__":
        import operator
        scan(operator.add,range(0,16))
        scan(operator.mul,range(1,17))
        scan(operator.add,list("hi world"))
        print [x for (x,f) in
                scan(segmented_sum,zip([7,6,5,4,3,2,1,0],
                                       [1,0,1,0,0,1,0,0]))]

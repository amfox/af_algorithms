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
# Retrieved from: http://en.literateprograms.org/Literate_Programming_(Python)?oldid=19169

import sys

if len(sys.argv) < 2:
    print "Usage: %s node" % sys.argv[0]
    sys.exit(1)

def findcode(file):
    cs, cur = ({}, None)
    for line in file.readlines():
        if line[0] is '@':    cur = line[1:-1]
        if line[0] is '>':    cs[cur] = cs.get(cur,"") + line[1:]
    return cs

def expand(node, cs):
    phase = True
    for x in cs[node][:-1].split('@'):
        if phase:    sys.stdout.write(x)
        else:        expand(x, cs)
        phase = not phase

expand(sys.argv[1], findcode(sys.stdin))

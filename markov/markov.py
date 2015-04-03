import string
successor = [("aL", "La", False),
             ("a0", "0a", False),
             ("a" , "b" , False),
             ("Lb", "b0", False),
             ("0b", "L" , True ),
             ("b" , "L" , True ),
             (""  , "a" , False)]
def contains(s, sub):
    return s.find(sub) != -1
def find_rule(a, w):
    try:
        return filter(lambda (l,r,b): contains(w, l), a)[0]
    except IndexError:
        raise ValueError, "not found"
def apply_rule((l,r,b), s):
    return s.replace(l, r, 1)
def apply_alg(a, w):
    l,r,b = r = find_rule(a, w)
    return apply_rule(r, w), b
def run(a, w):
    result = []
    flag = False                      # whether Halting rule was applied
    try:
        while not flag:               # Normal rule was applied
            result.append(w)
            w, flag = apply_alg(a, w) # apply a rule
        result.append(w)
    except ValueError:                # No rule was applied
        pass
    return result


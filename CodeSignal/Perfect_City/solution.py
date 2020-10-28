# [a, b], [c, d] = eval(dir()[0])

def perfectCity(*arr):
    [a, b], [c, d] = arr
    if a%1 == c%1 == 0:
        a, b, c, d = -b, a, -d, c # rotate
    if a//1 == c//1:
        a = 2*(a//1+(a + c - 2*(c//1) > 1)) - a # symmetry
    return abs(a - c) + abs(b - d)

"""
Usage: 
    *********************************************
    import mortonpy as m

    m.interleave(x, y, (optional) z)
    m.interleave2(x, y)
    m.interleave3(x, y, z)
    m.interleave_latlng(lat, lng)

    m.deinterleave2(n)
    m.deinterleave3(n)
    m.deinterleave_latlng(n)
    *********************************************

    In mathematical analysis and computer science, Z-order, Morton order,
    or Morton code is a function which maps multidimensional data to one
    dimension while preserving locality of the data points.
    
    It was introduced in 1966 by G. M. Morton.[1] The z-value of a point
    in multidimensions is simply calculated by interleaving the binary
    representations of its coordinate values.

    Once the data are sorted into this ordering, any one-dimensional
    data structure can be used such as binary search trees, B-trees,
    skip lists or (with low significant bits truncated) hash tables.
    The resulting ordering can equivalently be described as the order
    one would get from a depth-first traversal of a quadtree.

    (https://en.wikipedia.org/wiki/Z-order_curve)

Author:
    Trevor Prater (trevor.prater@gmail.com)
    MIT License

"""

global DIVISORS
DIVISORS = []
divisor = 180.0
for _ in range(32):
    DIVISORS.append(divisor)
    divisor /= 2.0
DIVISORS = tuple(DIVISORS)


def __part1by1(n):
    n &= 0x0000ffff
    n = (n | (n << 8))  & 0x00FF00FF
    n = (n | (n << 4))  & 0x0F0F0F0F
    n = (n | (n << 2))  & 0x33333333
    n = (n | (n << 1))  & 0x55555555
    return n


def __part1by2(n):
    n &= 0x000003ff
    n = (n ^ (n << 16)) & 0xff0000ff
    n = (n ^ (n << 8))  & 0x0300f00f
    n = (n ^ (n << 4))  & 0x030c30c3
    n = (n ^ (n << 2))  & 0x09249249
    return n


def __unpart1by1(n):
    n &= 0x55555555
    n = (n ^ (n >> 1))  & 0x33333333
    n = (n ^ (n >> 2))  & 0x0f0f0f0f
    n = (n ^ (n >> 4))  & 0x00ff00ff
    n = (n ^ (n >> 8))  & 0x0000ffff
    return n


def __unpart1by2(n):
    n &= 0x09249249
    n = (n ^ (n >> 2))  & 0x030c30c3
    n = (n ^ (n >> 4))  & 0x0300f00f
    n = (n ^ (n >> 8))  & 0xff0000ff
    n = (n ^ (n >> 16)) & 0x000003ff
    return n


def interleave2(*args):
    if len(args) != 2:
        raise ValueError('Usage: interleave2(x, y)')
    for arg in args:
        if not isinstance(arg, int):
            print 'Usage: interleave2(x, y)'
            raise ValueError("Supplied arguments contain a non-integer!")

    return __part1by1(args[0]) | (__part1by1(args[1]) << 1)


def interleave3(*args):
    if len(args) != 3:
        raise ValueError('Usage: interleave3(x, y, z)')
    for arg in args:
        if not isinstance(arg, int):
            print 'Usage: interleave3(x, y, z)'
            raise ValueError("Supplied arguments contain a non-integer!")

    return __part1by2(args[0]) | (__part1by2(args[1]) << 1) | (
        __part1by2(args[2]) << 2)


def interleave(*args):
    if len(args) < 2 or len(args) > 3:
        print('Usage: interleave(x, y, (optional) z)')
        raise ValueError(
            "You must supply two or three integers to interleave!")

    method = globals()["interleave" + str(len(args))]
    return method(*args)


def interleave_latlng(lat, lng):
    if (lng > 180):
        x = (lng % 180) + 180.0
    elif (lng < -180):
        x = (-((-lng) % 180)) + 180.0
    elif (lng == 180):
        x = 0.0
    else:
        x = lng + 180.0
    if (lat > 90):
        y = (lat % 90) + 90.0
    elif (lat < -90):
        y = (-((-lat) % 90)) + 90.0
    elif (lat == 90):
        y = lat - (DIVISORS[len(DIVISORS) - 1] / 2.0) + 90.0
    else:
        y = lat + 90.0

    mortonCode = ""
    for dx in DIVISORS:
        digit = 0
        if (y >= dx):
            digit |= 2
            y -= dx
        if (x >= dx):
            digit |= 1
            x -= dx
        mortonCode += str(digit)
    return mortonCode


def deinterleave2(n):
    if not isinstance(n, int):
        print 'Usage: deinterleave2(n)'
        raise ValueError("Supplied arguments contain a non-integer!")
    return __unpart1by1(n), __unpart1by1(n >> 1)


def deinterleave3(n):
    if not isinstance(n, int):
        print 'Usage: deinterleave2(n)'
        raise ValueError("Supplied arguments contain a non-integer!")
    return __unpart1by2(n), __unpart1by2(n >> 1), __unpart1by2(n >> 2)


def deinterleave_latlng(n):
    x = y = 0
    for (digit, multiplier) in zip([int(d) for d in n], DIVISORS):
        if (digit & 2):
            y += multiplier
        if (digit & 1):
            x += multiplier
    return y - 90.0, x - 180.0


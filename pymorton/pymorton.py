# pymorton (https://github.com/trevorprater/pymorton)
# Author: trevor.prater@gmail.com
# License: MIT

import sys

_DIVISORS = [180.0 / 2 ** n for n in range(32)]


def __part1by1_32(n):
    n &= 0x0000ffff                  # base10: 65535,      binary: 1111111111111111,                 len: 16
    n = (n | (n << 8))  & 0x00FF00FF # base10: 16711935,   binary: 111111110000000011111111,         len: 24
    n = (n | (n << 4))  & 0x0F0F0F0F # base10: 252645135,  binary: 1111000011110000111100001111,     len: 28
    n = (n | (n << 2))  & 0x33333333 # base10: 858993459,  binary: 110011001100110011001100110011,   len: 30
    n = (n | (n << 1))  & 0x55555555 # base10: 1431655765, binary: 1010101010101010101010101010101,  len: 31

    return n


def __part1by2_32(n):
    n &= 0x000003ff                  # base10: 1023,       binary: 1111111111,                       len: 10
    n = (n ^ (n << 16)) & 0xff0000ff # base10: 4278190335, binary: 11111111000000000000000011111111, len: 32
    n = (n ^ (n << 8))  & 0x0300f00f # base10: 50393103,   binary: 11000000001111000000001111,       len: 26
    n = (n ^ (n << 4))  & 0x030c30c3 # base10: 51130563,   binary: 11000011000011000011000011,       len: 26
    n = (n ^ (n << 2))  & 0x09249249 # base10: 153391689,  binary: 1001001001001001001001001001,     len: 28

    return n


def __unpart1by1_32(n):
    n &= 0x55555555                  # base10: 1431655765, binary: 1010101010101010101010101010101,  len: 31
    n = (n ^ (n >> 1))  & 0x33333333 # base10: 858993459,  binary: 110011001100110011001100110011,   len: 30
    n = (n ^ (n >> 2))  & 0x0f0f0f0f # base10: 252645135,  binary: 1111000011110000111100001111,     len: 28
    n = (n ^ (n >> 4))  & 0x00ff00ff # base10: 16711935,   binary: 111111110000000011111111,         len: 24
    n = (n ^ (n >> 8))  & 0x0000ffff # base10: 65535,      binary: 1111111111111111,                 len: 16

    return n


def __unpart1by2_32(n):
    n &= 0x09249249                  # base10: 153391689,  binary: 1001001001001001001001001001,     len: 28
    n = (n ^ (n >> 2))  & 0x030c30c3 # base10: 51130563,   binary: 11000011000011000011000011,       len: 26
    n = (n ^ (n >> 4))  & 0x0300f00f # base10: 50393103,   binary: 11000000001111000000001111,       len: 26
    n = (n ^ (n >> 8))  & 0xff0000ff # base10: 4278190335, binary: 11111111000000000000000011111111, len: 32
    n = (n ^ (n >> 16)) & 0x000003ff # base10: 1023,       binary: 1111111111,                       len: 10

    return n


def __part1by1_64(n):
    n &= 0x00000000ffffffff                  # binary: 11111111111111111111111111111111,                                len: 32
    n = (n | (n << 16)) & 0x0000FFFF0000FFFF # binary: 1111111111111111000000001111111111111111,                        len: 40
    n = (n | (n << 8))  & 0x00FF00FF00FF00FF # binary: 11111111000000001111111100000000111111110000000011111111,        len: 56
    n = (n | (n << 4))  & 0x0F0F0F0F0F0F0F0F # binary: 111100001111000011110000111100001111000011110000111100001111,    len: 60
    n = (n | (n << 2))  & 0x3333333333333333 # binary: 11001100110011001100110011001100110011001100110011001100110011,  len: 62
    n = (n | (n << 1))  & 0x5555555555555555 # binary: 101010101010101010101010101010101010101010101010101010101010101, len: 63

    return n


def __part1by2_64(n):
    n &= 0x1fffff                            # binary: 111111111111111111111,                                         len: 21
    n = (n | (n << 32)) & 0x1f00000000ffff   # binary: 11111000000000000000000000000000000001111111111111111,         len: 53
    n = (n | (n << 16)) & 0x1f0000ff0000ff   # binary: 11111000000000000000011111111000000000000000011111111,         len: 53
    n = (n | (n << 8))  & 0x100f00f00f00f00f # binary: 1000000001111000000001111000000001111000000001111000000001111, len: 61
    n = (n | (n << 4))  & 0x10c30c30c30c30c3 # binary: 1000011000011000011000011000011000011000011000011000011000011, len: 61
    n = (n | (n << 2))  & 0x1249249249249249 # binary: 1001001001001001001001001001001001001001001001001001001001001, len: 61

    return n


def __unpart1by1_64(n):
    n &= 0x5555555555555555                  # binary: 101010101010101010101010101010101010101010101010101010101010101, len: 63
    n = (n ^ (n >> 1))  & 0x3333333333333333 # binary: 11001100110011001100110011001100110011001100110011001100110011,  len: 62
    n = (n ^ (n >> 2))  & 0x0f0f0f0f0f0f0f0f # binary: 111100001111000011110000111100001111000011110000111100001111,    len: 60
    n = (n ^ (n >> 4))  & 0x00ff00ff00ff00ff # binary: 11111111000000001111111100000000111111110000000011111111,        len: 56
    n = (n ^ (n >> 8))  & 0x0000ffff0000ffff # binary: 1111111111111111000000001111111111111111,                        len: 40
    n = (n ^ (n >> 16)) & 0x00000000ffffffff # binary: 11111111111111111111111111111111,                                len: 32
    return n


def __unpart1by2_64(n):
    n &= 0x1249249249249249                  # binary: 1001001001001001001001001001001001001001001001001001001001001, len: 61
    n = (n ^ (n >> 2))  & 0x10c30c30c30c30c3 # binary: 1000011000011000011000011000011000011000011000011000011000011, len: 61
    n = (n ^ (n >> 4))  & 0x100f00f00f00f00f # binary: 1000000001111000000001111000000001111000000001111000000001111, len: 61
    n = (n ^ (n >> 8))  & 0x1f0000ff0000ff   # binary: 11111000000000000000011111111000000000000000011111111,         len: 53
    n = (n ^ (n >> 16)) & 0x1f00000000ffff   # binary: 11111000000000000000000000000000000001111111111111111,         len: 53
    n = (n ^ (n >> 32)) & 0x1fffff           # binary: 111111111111111111111,                                         len: 21
    return n


if sys.version_info[0] == 2 and getattr(sys, 'maxint', 0) and sys.maxint <= 2 ** 31 - 1:
    __part1by1 = __part1by1_32
    __part1by2 = __part1by2_32
    __unpart1by1 = __unpart1by1_32
    __unpart1by2 = __unpart1by2_32
else:
    __part1by1 = __part1by1_64
    __part1by2 = __part1by2_64
    __unpart1by1 = __unpart1by1_64
    __unpart1by2 = __unpart1by2_64


def interleave2(*args):
    if len(args) != 2:
        raise ValueError('Usage: interleave2(x, y)')
    for arg in args:
        if not isinstance(arg, int):
            print('Usage: interleave2(x, y)')
            raise ValueError("Supplied arguments contain a non-integer!")

    return __part1by1(args[0]) | (__part1by1(args[1]) << 1)


def interleave3(*args):
    if len(args) != 3:
        raise ValueError('Usage: interleave3(x, y, z)')
    for arg in args:
        if not isinstance(arg, int):
            print('Usage: interleave3(x, y, z)')
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


def deinterleave2(n):
    if not isinstance(n, int):
        print('Usage: deinterleave2(n)')
        raise ValueError("Supplied arguments contain a non-integer!")

    return __unpart1by1(n), __unpart1by1(n >> 1)


def deinterleave3(n):
    if not isinstance(n, int):
        print('Usage: deinterleave2(n)')
        raise ValueError("Supplied arguments contain a non-integer!")

    return __unpart1by2(n), __unpart1by2(n >> 1), __unpart1by2(n >> 2)

def interleave_latlng(lat, lng):
    if not isinstance(lat, float) or not isinstance(lng, float):
        print('Usage: interleave_latlng(float, float)')
        raise ValueError("Supplied arguments must be of type float!")

    if (lng > 180):
        x = (lng % 180) + 180.0
    elif (lng < -180):
        x = (-((-lng) % 180)) + 180.0
    else:
        x = lng + 180.0
    if (lat > 90):
        y = (lat % 90) + 90.0
    elif (lat < -90):
        y = (-((-lat) % 90)) + 90.0
    else:
        y = lat + 90.0

    morton_code = ""
    for dx in _DIVISORS:
        digit = 0
        if (y >= dx):
            digit |= 2
            y -= dx
        if (x >= dx):
            digit |= 1
            x -= dx
        morton_code += str(digit)

    return morton_code


def deinterleave_latlng(n):
    x = y = 0
    for (digit, multiplier) in zip([int(d) for d in n], _DIVISORS):
        if (digit & 2):
            y += multiplier
        if (digit & 1):
            x += multiplier

    return round(y - 90.0, 6), round(x - 180.0, 6)


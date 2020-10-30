#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Easter is the first Sunday after the ecclesastical (not astronomical) full moon
that happens on or next after the March equinox.
Reference: Meuss, Jean: Astronomical Algorithms, page 67.
"""

from math import floor


def easter(year: int):
    """
    Return the date of Easter for the given Gregorian calendar year (after October 1583)
    n = month number (3 = March, 4 = April).
    p + 1 = Day of the month on which Easter Sunday falls.
    The extreme dates of Easter are MArch 22 (1818, 2285) and April 25 (1886, 1943, 2038).
    """
    a = year % 19
    b = floor(year / 100)
    c = year % 100
    d = floor(b / 4)
    e = b % 4
    f = floor((b + 8) / 25)
    g = floor((b - f + 1) / 3)
    h = (19 * a + b - d - g + 15) % 30
    i = floor(c / 4)
    k = c % 4
    l = (32 + 2 * e + 2 * i - h - k) % 7
    m = floor((a + 11 * h + 22 * l) / 451)
    n = floor((h + l - 7 * m + 114) / 31)
    p = (h + l - 7 * m + 114) % 31
    return n, p + 1


if __name__ == '__main__':
    # examples from Meeus, page 68
    assert easter(1818) == (3, 22)
    assert easter(1954) == (4, 18)
    assert easter(1991) == (3, 31)
    assert easter(1992) == (4, 19)
    assert easter(1993) == (4, 11)
    assert easter(2000) == (4, 23)
    assert easter(2020) == (4, 12)
    assert easter(2021) == (4, 4)

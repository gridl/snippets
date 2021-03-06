#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#
# Advent of Code, Day 04 - Part 1 & 2
# https://github.com/vesche
#

import hashlib
import itertools


def md5hash(string, x):
    m = hashlib.md5()
    m.update(string)
    return m.hexdigest()[0:x]


def main():
    secret = "ckczppom"

    for n in itertools.count():
        if md5hash(secret + str(n), 5) == "00000":
            part_one = n
            break

    for n in itertools.count():
        if md5hash(secret + str(n), 6) == "000000":
            part_two = n
            break

    print "Part One: {0}, Part Two: {1}".format(part_one, part_two)


if __name__ == "__main__":
    main()

#!/usr/bin/env python
# -*- coding: utf-8 -*-

# [s]tring rune


def info(_):
    from common import list_functions
    return "[s]tring rune\nactions: {}".format(list_functions(__name__))

def length(string):
    return len(string)

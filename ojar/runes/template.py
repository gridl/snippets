#!/usr/bin/env python
# -*- coding: utf-8 -*-

# [?] rune


def info(_):
    from common import list_functions
    return "[?] rune\nactions: {}".format(list_functions(__name__))

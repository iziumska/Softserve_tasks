# !/usr/bin/env python

import sys


def is_validation_argv():
    return len(sys.argv) == 3 or len(sys.argv) == 4

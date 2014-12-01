#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 02: Lesson 14"""

import numpy
from pprint import pprint


def numpy_task02(param_mean, param_sd, rep):
    """list of normally distributed random numbers
    this will be helpful for modeling and statistical analysis """

    return [numpy.random.normal(param_mean, param_sd, rep)]

if __name__ == "__main__":
    pprint(numpy_task02(100, 10, 100))
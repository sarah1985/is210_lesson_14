#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 02: Lesson 14"""

import numpy
from pprint import pprint


def numpy_task02(param_mean, param_sd):
    """list of normally distributed random numbers
    this will be helpful for modeling and statistical analysis """

    normal_list = []
    for num in range(1, 100):
        normal_list.append(numpy.random.normal(param_mean, param_sd))

    return normal_list

if __name__ == "__main__":
    pprint(numpy_task02(100, 10))
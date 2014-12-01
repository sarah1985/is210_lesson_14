#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 03: Lesson 14"""

import numpy


def numpy_task03(txt_file):
    """Calculate mean and s.d. of values in document"""

    try:
        input_file = numpy.loadtxt(txt_file)
        file_mean = int(numpy.mean(input_file))
        file_std = int(numpy.std(input_file))
        result = (file_mean, file_std)

    except IOError:
        print "There was an error opening {}.".format(txt_file)

    else:
        return result
    print "Success! Here are your calculations: \n" \
          "Mean: {} \n" \
          "Standard Deviation: {}".format(result[0], result[1])

if __name__ == "__main__":
    print numpy_task03('data.txt')
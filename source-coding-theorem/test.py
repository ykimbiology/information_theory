#! /usr/bin/python


"""
INPUT:
  1) N: 

Define a probability distribution function.
  P(x) =p0^(N-r(x))p1^r(x)
  r(x) = number of 1s in x.

"""

import math

def get_example_x():
    #x = [0,1,0,1,1]
    x = [0,1]
    return x

def get_probability(x, p0=0.9, p1=0.1):
    N = len(x)
    count_ones = sum(x)
    px = pow(p0, N - count_ones)*pow(p1, count_ones)
    return px

def test_get_probability():
    """
    nosetests test.py
    """
    cutoff_error = 0.000001
    x = get_example_x()
    prob = get_probability(x)
    error = abs(prob - 0.09)
    print prob, error
    assert error < cutoff_error
    #assert False

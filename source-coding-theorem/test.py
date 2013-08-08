#! /usr/bin/python


"""
INPUT:
  1) N: 

Define a probability distribution function.
  P(x) =p0^(N-r(x))p1^r(x)
  r(x) = number of 1s in x.

"""

import math

import numpy as np
import matplotlib.pyplot as plt

def get_example_x():
    #x = [0,1,0,1,1]
    x = [0,1]
    return x

def bin(s):
    """
    Taken from: http://wiki.python.org/moin/BitManipulation
    >>>bin(0)
    '0'
    >>>bin(2)
    '10'
    """
    return str(s) if s<=1 else bin(s>>1) + str(s&1)

def get_binary_vector_list(n):
    """
    n = length of a vector.
    OUTPUT:
      A list of all possible binary vector.
    """
    count_vectors = pow(2, n) # 2^n;
    xlist = []
    for idx in range(count_vectors):
        x = bin(idx)
        xlist.append(x)
    return xlist

def get_probability(x, N, p0=0.9, p1=0.1):
    """
    INPUT:
      N: size of the binary vector.
    """
    count_ones = sum([1 for xi in x if xi=='1'])
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
    #print prob, error
    assert error < cutoff_error
    #assert False

def get_entropy_ensemble(content, delta):
    """
    INPUT
      content: sorted from high to low prob.
    """
    prob_sum = 0.0
    xlist_subset = []
    for (v, prob) in content:
        prob_sum = prob_sum + prob
        if (prob_sum > (1 - delta)): break
        xlist_subset.append((v,prob))
    #print len(xlist_subset), len(xlist)
    entropy_delta = None
    if len(xlist_subset) > 0:
        entropy_delta = math.log(len(xlist_subset), 2)
    return entropy_delta

def get_entropy_delta(n, content, delta):

    entropy_delta = get_entropy_ensemble(content, delta)
    #print delta, entropy_delta
    return entropy_delta

if __name__ == '__main__':
    n = 10
    d_list = np.arange(0,1,0.01)
    xlist = get_binary_vector_list(n)
    problist = [get_probability(x, n) for x in xlist]
    content = zip(xlist, problist)
    content = sorted(content, key=lambda (v, prob): prob, reverse=True)
    delta_ent_list = []
    for delta in d_list:
        entropy = get_entropy_delta(n, content, delta)
        if entropy != None:
            delta_ent_list.append((delta, entropy))
            print delta, entropy
    delta_ent_list = np.array(delta_ent_list)
    plt.scatter(delta_ent_list[:,0], delta_ent_list[:,1])
    plt.plot(delta_ent_list[:,0], delta_ent_list[:,1])
    plt.xlabel('delta')
    plt.ylabel('H_delta(X^N)')
    plt.show()
        

# -*- coding: utf-8 -*-

import math

#vector_subtract comment
def vector_subtract(v,w):
    return [v_i - w_i
            for v_i, w_i in zip(v,w)]

#vector dot product comment
def dot(v,w):
    return sum(v_i*w_i
               for v_i, w_i in zip(v,w))
    
def sum_of_squares(v):
    return dot(v,v)

def squared_distance(v,w):
    return sum_of_squares(vector_subtract(v,w))

def distance(v,w):
    return math.sqrt(squared_distance(v,w))

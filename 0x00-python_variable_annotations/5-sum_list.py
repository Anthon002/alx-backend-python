#!/usr/bin/env python3
'''This module contains the sum_list function.
'''
from typing import List


def sum_list(input_list: List[float]) -> float:
    '''Computes the sum of a list of floating-point numbers.
    '''
    sum = float(sum(input_list))
    return sum

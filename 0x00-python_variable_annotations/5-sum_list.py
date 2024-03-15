#!/usr/bin/env python3
'''This module contains the sum_list function.
'''
from typing import List


def sum_list(input_list: List[float]) -> float:
    '''This calcs the sum of a list of floats.
    '''
    sum_ = float(sum(input_list))
    return sum_

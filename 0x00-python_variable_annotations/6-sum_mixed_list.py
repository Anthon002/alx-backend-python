#!/usr/bin/env python3
'''This module function sum_mixed_list.
'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''This module will calc the sum of an int list of floating-point numbers.
    '''
    sum_ = float(sum(mxd_lst))
    return sum_

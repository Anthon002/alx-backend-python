#!/usr/bin/env python3
'''This module function make_multiplier.
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''This module will create a multiplier function.
    '''
    multiplier_ = lambda x: x * multiplier
    return multiplier_ 

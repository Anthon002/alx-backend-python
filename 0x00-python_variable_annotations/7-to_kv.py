#!/usr/bin/env python3
'''This module's function to_kv.
'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''This method will convert a key value to a tuple.
    '''
    convert_ = k, float(v**2)
    return convert_

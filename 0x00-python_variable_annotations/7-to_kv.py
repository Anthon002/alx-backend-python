#!/usr/bin/env python3
'''This module's function to_kv.
'''
from typing import Union, Tuple


def kv_to_tuple(data: Tuple[str, Union[int, float]]) -> Tuple[str, float]:
  """This method will unpack a tuple containing a key and its value, 
  and return a new tuple of the key and the square of the value.
  """
  key, value = data
  return key, float(value**2)

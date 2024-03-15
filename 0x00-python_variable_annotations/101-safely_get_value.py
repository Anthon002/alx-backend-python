#!/usr/bin/env python3
'''This module's function safely_get_value.
'''
from typing import Mapping, TypeVar, Any, Union


TypeVar_ = TypeVar('T')
res_ = Union[Any, TypeVar_]
Def = Union[TypeVar_, None]


def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> res_:
    '''Retrieves a value from a dict using a given key.
    '''
    if key in dct:
        dict_ = dct[key]
        return dict_
    return default
